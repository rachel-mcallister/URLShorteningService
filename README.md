## how to run url shortening service
1. set up virtual environment (windows - py -m pip install --user virtualenv
 && py -m venv env && .\env\Scripts\activate
 to activate)
2. pip install -r requirements.txt present in the root dir
3. python app.py
4. enter a url to be shortened and press go
5. you can also enter the short id you would like to use 

## all_urls
this returns all urls present in the database
take any sort code and put it at the end of the present url



CASES **
1 case - user sends log url -> send back short url

get long url and check if it already exists 
1. if it does return short version of it
2. if it does not need to create a new code (three random letters)

2 short url - redirect to the long url which that short corresponds to# firstURLShorteningService
