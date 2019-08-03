import unittest


class GeneralTestCase(unittest.TestCase):

    def __init__(self, methodName, param1=None, param2=None):
        super(GeneralTestCase, self).__init__(methodName)
        self.param1 = param1
        self.param2 = param2

    def runTest(self):
        self.assertEqual(self.param1, self.param2, self._testMethodName+" vida hpppppppppp")


def load_tests(loader, tests, pattern):
    test_cases = unittest.TestSuite()
    for p1, p2 in [(2, 5), (5, 3)]:
        test_cases.addTest(GeneralTestCase('runTest', p1, p2))
    return test_cases

    # unittest.main()