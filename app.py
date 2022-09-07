import os
import sqlite3
import string
from random import choice

import flask
from flask import (
    Flask,
    render_template, request, redirect, session, url_for, make_response, jsonify, json
)

app = Flask(__name__, template_folder="templates")

db = "MyUrlsDB.db"
connection = sqlite3.connect(db, check_same_thread=False)
cursor = connection.cursor()


def generateRandomString(length_of_string):
    # choose from all lowercase and upper case characters as well as digits
    while True:
        letters = string.ascii_lowercase + string.ascii_uppercase
        digits = string.digits
        result_str = ''.join(choice(letters + digits) for i in range(length_of_string))
        # make sure the value does not already exist
        cursor.execute("SELECT url_id FROM urls WHERE short_url = ?", (result_str,))
        data = cursor.fetchall()
        if len(data) == 0:
            return result_str


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        # use the name used in the form in html (URL) to retrieve long url entered
        url_from_form = request.form["url"]

        # check if long URL exists in DB
        cursor.execute("SELECT short_url FROM urls WHERE long_url = ?", (url_from_form.strip(),))
        data = cursor.fetchall()

        if len(data) != 0:
            # return short URL if found i.e. data found is not null
            existing_short_url = data[0][0]
            return render_template("shorturl.html", short_url_to_display=existing_short_url)

        # else -> create new code, store in DB and return the new shortened URL
        else:
            new_short_url = generateRandomString(8)
            print(new_short_url)

            sql = "INSERT INTO urls (long_url, short_url) VALUES(?, ?)"
            cursor.execute(sql, (url_from_form, new_short_url))
            print("new URL added to the DB")
            # commit changes and close the cursor **
            connection.commit()
            return render_template("shorturl.html", short_url_to_display=new_short_url)


# shorturl.html page executes this app.route
# if the short exists gets the long from it and redirects to that long URL **
@app.route('/<short_url>')
def redirecting(short_url):
    cursor.execute("SELECT long_url FROM urls WHERE short_url = ?", (short_url,))
    data = cursor.fetchall()
    if len(data) != 0:
        # redirect to long URL
        return redirect(data[0][0])
    else:
        return returnResponse('URL does not exist', 400)


# returns all URL that have been shortened by accessing the DB
@app.route("/getAllUrls")
def get_all_urls():
    cursor.execute("SELECT * FROM urls")

    results = cursor.fetchall()
    # str1 = ''.join(str(e) for e in results)
    return render_template("allUrls.html", data=results)


def returnResponse(string, status_code):
    response = flask.Response(string, status=status_code)
    response.headers["Content-Type"] = "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == '__main__':
    os.system("python3 create_database_and_tables.py")
    app.run(host="0.0.0.0", port=5000, debug=True)
