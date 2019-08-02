from flask import Flask, request

from testing.silver_test import app
import unittest


class DynamicUnitTestContainer(unittest.TestCase):

    def __init__(self, methodName, param1=None, param2=None):
        super(DynamicUnitTestContainer, self).__init__(methodName)
        self.param1 = param1
        self.param2 = param2

    def test_rest_endpoint(self):

        app.testing = True
        client = app.test_client()

        id = str(self.param1)
        param = self.param2

        with client:
            rv = client.get('/basic/'+id, query_string={'param': param})
            print(rv._status_code)
            self.assertEqual(rv._status_code, 305, "hablando mierda")


def load_tests(loader, tests, pattern):
    test_cases = unittest.TestSuite()
    for p1, p2 in [(2, "hola"), (5, "chaooo")]:
        test_cases.addTest(DynamicUnitTestContainer('test_rest_endpoint', p1, p2))
    return test_cases




    unittest.main()