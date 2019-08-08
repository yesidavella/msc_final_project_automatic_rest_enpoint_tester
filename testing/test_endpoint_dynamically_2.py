from flask import Flask, request

from silver_test import app
import unittest
import inspect


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
                self.assertEqual(rv._status_code, 305, "Failed in test with name: "+description)

        return test_rest_endpoint


def main():
    # testsmap = [('foo', 1, "111111"), ('bar', 2, "2222222222"), ('goo', 3, "333333333"), ('doo', -1, "-111111")]
    testsmap = [('foo', 1, "111111"), ('bar', 2, "2222222222"), ('goo', 3, "333333333")]
    # testsmap = [('foo', 1, "valorparammmmmm")]

    for test_name, id, param in testsmap:
        # print("forrrrrrrrrrrrrrrrrrr")
        klassname = 'Test_{0}'.format(test_name)
        method_name = 'test_gen_{0}'.format(test_name)
        test_func = TestProvider.make_test_function(klassname, id, param)
        globals()[klassname] = type(klassname, (DynamicClassBase,),{method_name: test_func})
        # func_lines = inspect.getsource(test_func).co_code
        # print(func_lines)


    unittest.main()

main()

# def suite():
#     suite = unittest.TestSuite()
#     suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestApp))
#
#     return suite
#
#
# if __name__ == "__main__":
#     unittest.TextTestRunner(verbosity=2).run(suite())
# Execute this with this command:
# wrong /home/yesid/OneDrive/msc_project/py3_venv/bin/python -m unittest testing/test_endpoint_dynamically_2.py
#
# TO EXECUTEEEEEEEEEEEEE
#
# coverage run test_endpoint_dynamically_2.py
# coverage xml

# coverage run --source=silver_test test_endpoint_dynamically_2.py
#  coverage report -m
