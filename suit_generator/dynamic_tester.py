import logging
import sys
import parameter_caster
from endpoint import app
import unittest

logging.basicConfig(filename='../logs/dynamic_tester.log', level=logging.DEBUG)


class DynamicClassBase(unittest.TestCase):
    longMessage = True


class TestProvider:

    def make_test_function(**kwargs):

        def test_rest_endpoint(self):
            app.testing = True
            client = app.test_client()

            with client:
                resp = client.get('/basicget/' + str(kwargs["id"]), query_string={'limit': str(kwargs["limit"])})
                print(resp._status_code)
                self.assertEqual(resp._status_code, 200, "Failed in test with name: "+kwargs["id"])

        return test_rest_endpoint


def main(argv):
    logging.debug("Entering to execution argv: " + str(argv))
    tuple_list_params = parameter_caster.ger_params_as_tuple_list(argv)
    logging.info("Array of tuples of argv: " + str(tuple_list_params))

    mapping = {}
    for param_pos, param_name, param_value in tuple_list_params:
        mapping[param_name] = param_value

    logging.info("Arguments to be inserted in the method: " + str(mapping))
    method_name = 'test_rest_endpoint'
    klassname = 'test_gen_{0}'.format(method_name)

    test_func = TestProvider.make_test_function(**mapping)

    try:
        globals()[klassname] = type(klassname, (DynamicClassBase,), {method_name: test_func})
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    except Exception:
        logging.info("Exception trying to execute unit test {}".format(Exception))


main(sys.argv)