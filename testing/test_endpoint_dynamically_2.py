from flask import Flask, request

from testing.silver_test import app
import unittest

class DynamicClassBase(unittest.TestCase):
    longMessage = True


class TestProvider:

    def make_test_function(description, id, param):

        def test_rest_endpoint(self):
            app.testing = True
            client = app.test_client()

            # id = str(self.param1)
            # param = self.param2

            with client:
                rv = client.get('/basic/' + str(id), query_string={'param': str(param)})
                print(rv._status_code)
                self.assertEqual(rv._status_code, 303, "hablando mierda")

        return test_rest_endpoint


def main():
    testsmap = [('foo', 1, "111111"), ('bar', 2, "2222222222"), ('goo', 3, "333333333")]

    for test_name, id, param in testsmap:
        print("forrrrrrrrrrrrrrrrrrr")
        test_func = TestProvider.make_test_function("genericoo", id, param)
        klassname = 'Test_{0}'.format(test_name)
        method_name = 'test_gen_{0}'.format(test_name)
        globals()[klassname] = type(klassname, (DynamicClassBase,),{method_name: test_func})


main()
# Execute this with this command:
#     /home/yesid/OneDrive/msc_project/py3_venv/bin/python -m unittest testing/test_endpoint_dynamically_2.py