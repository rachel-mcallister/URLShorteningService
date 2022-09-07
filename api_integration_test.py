from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class URLShortenerHomePage:

    URL:'https://127.0.0.1/5000'

    SEARCH_INPUT = (By.NAME, 'q');

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL);



