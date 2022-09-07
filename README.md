## How to run URL shortening service
1. Set up virtual environment (```windows- py -m venv env``` && ```.\env\Scripts\activate``` to activate)
2. ```pip install -r requirements.txt``` present in the root dir
3. ```python app.py```
4. Enter a URL to be shortened and press shorten URL button
5. You can also press the Get All URLs button to view all existing shortened URLs

## CASES 
Get long URL that user has entered and check if it already exists in the database
1. If it does return the Short URL of it
2. If it does not need to create a new code (eight random letters) to become the Short URL for it

Use the Short URL in either case to redirect to the Long Url which that short corresponds to

## Tests 
Functional tests present in testapp_functional_tests.py file which contains all fucntional tests
test.py file is used to test the generate random string method used for generating the Short URLs
