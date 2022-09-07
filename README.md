## how to run url shortening service
1. set up virtual environment (windows- py -m venv env && .\env\Scripts\activate to activate)
2. pip install -r requirements.txt present in the root dir
3. python app.py
4. enter a url to be shortened and press shorten URL button
5. You can also press the Get All URLs button to view all existing shortened URLs

CASES **
Get long url that user has entered and check if it already exists in the database
1. if it does return Short URL  of it
2. if it does not need to create a new code (eight random letters) to become the Short URL for it

Use the Short URL in either case to redirect to the Long Url which that short corresponds to
