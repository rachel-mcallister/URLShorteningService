import unittest
import app


class TestGenerateRandomString(unittest.TestCase):

    def test_generateRandomString(self):
        result = app.generateRandomString(8)
        self.assertTrue(len(result) == 8)


if __name__ == '__main__':
    unittest.main()
