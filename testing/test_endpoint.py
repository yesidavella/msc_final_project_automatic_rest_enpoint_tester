from flask import Flask, request

from testing.silver_test import app
import unittest

class FinalTest(unittest.TestCase):

    def test_bar(self):

        app.testing = True
        client = app.test_client()

        with client:
            rv = client.get('/basic/45', query_string={'param': 'ccccccccccc'})
            print(rv._status_code)
            self.assertEqual(rv._status_code, 303, "hablando mierda")


# if __name__ == "__main__":
unittest.main()