# script used to create database tables
import sqlite3

from flask import Flask

script = Flask(__name__)
# define connection and cursor

connection = sqlite3.connect('MyUrlsDB.db', check_same_thread=False)

cursor = connection.cursor()

# create table to store url in
command1 = """CREATE TABLE IF NOT EXISTS
    urls(url_id INTEGER PRIMARY KEY, long_url INTEGER, short_url INTEGER)"""

cursor.execute(command1)