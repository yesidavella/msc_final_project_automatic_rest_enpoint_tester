import unittest


class DynamicClassBase(unittest.TestCase):
    longMessage = True


class TestProvider:
    def make_test_function(description, a, b):
        def test(self):
            print("Assertttttttttttttttttttt")
            self.assertEqual(a, b, description)
        return test


def main():
    testsmap = {
        'foo': [1, 2],
        'bar': [2, 4],
        'goo': [1, 2],
        'tar': [2, 4],
        'moo': [1, 2],
        'yar': [2, 8],}

    for name, params in testsmap.items():
        print("forrrrrrrrrrrrrrrrrrr")
        test_func = TestProvider.make_test_function(name, params[0], params[1])
        klassname = 'Test_{0}'.format(name)
        method_name = 'test_gen_{0}'.format(name)
        globals()[klassname] = type(klassname, (DynamicClassBase,),{method_name: test_func})


    # suite = unittest.TestLoader().loadTestsFromTestCase(DynamicClassBase)
    # unittest.TextTestRunner(verbosity=2).run(suite)

main()
