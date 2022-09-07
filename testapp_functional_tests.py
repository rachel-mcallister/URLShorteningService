import sqlite3
import unittest

from app import app


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_route_mapping(self):
        response = self.app.get('/')
        assert response.status_code == 200
        assert b"shorten URL" in response.data
        assert b"Enter a URL:" in response.data

    def test_home_page_post_with_url_that_does_not_exist(self):
        long_url = 'https://blog.miguelgrinberg.com/post/how-to-write-unit-tests-in-python-part-3-web-applications'
        response = self.app.post('/', data={
            'url': long_url},
                                 follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == '/'
        assert b"http://127.0.0.1:5000/" in response.data
        assert b"BACK TO HOME" in response.data

        # check its added to db
        db = "MyUrlsDB.db"
        connection = sqlite3.connect(db, check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute("SELECT short_url FROM urls WHERE long_url = ?", (long_url.strip(),))

        results = cursor.fetchall()
        assert len(results) != 0

    def test_home_page_post_with_url_that_does_exist(self):
        existing_URL = 'https://docs.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/'
        response = self.app.post('/', data={
            'url': existing_URL},
                                 follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == '/'
        assert b"http://127.0.0.1:5000/" in response.data
        assert b"BACK TO HOME" in response.data

    # short url endpoint
    def test_short_url_that_does_not_exist(self):
        response = self.app.get('/aaaa')
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert response.data.decode("utf-8") == 'URL does not exist'
        assert b"URL does not exist" in response.data

    def test_short_url_that_does_exist(self):
        response = self.app.get('/Y1Smd4cI')
        # moved to the next page
        assert response.status_code == 302
        assert b"Redirecting" in response.data
        assert b"https://docs.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/" in response.data

    def test_get_AllUrls(self):
        response = self.app.get('/getAllUrls')
        # moved to the next page
        assert response.status_code == 200
        # all fields in table are present
        assert b"URL id" in response.data
        assert b"Long URL" in response.data
        assert b"Short URL" in response.data


if __name__ == '__main__':
    unittest.main()
