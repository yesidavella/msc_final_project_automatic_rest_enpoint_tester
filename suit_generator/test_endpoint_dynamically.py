from main_endpoint import app
import unittest, sys, parameter_caster, logging


class DynamicClassBase(unittest.TestCase):
    longMessage = True


class TestProvider:

    def make_test_function(description, id, param):

        def test_rest_endpoint(self):
            app.testing = True
            client = app.test_client()

            with client:
                rv = client.get('/basicget/' + str(id), query_string={'param': str(param)})
                print(rv._status_code)
                self.assertEqual(rv._status_code, 200, "Failed in test with name: "+description)

        return test_rest_endpoint


def main(argv):

    logging.basicConfig(filename='test_endpoint_dynamically.log', level=logging.DEBUG)
    logging.info("argv" + str(argv))
    tuple_list_params = parameter_caster.ger_params_as_tuple_list(argv)
    # testsmap = [('foo', 1, "111111"), ('bar', 2, "2222222222"), ('goo', 3, "333333333")]
    logging.info("argv" + str(tuple_list_params))

    for test_name, id, param in tuple_list_params:
        klassname = 'Test_{0}'.format(test_name)
        method_name = 'test_gen_{0}'.format(test_name)
        test_func = TestProvider.make_test_function(klassname, id, param)
        globals()[klassname] = type(klassname, (DynamicClassBase,),{method_name: test_func})
        # func_lines = inspect.getsource(test_func).co_code
        # print(func_lines)

    unittest.main()

main(sys.argv)
