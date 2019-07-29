import testing.Foo
from testing.Foo import Foo
import unittest


class FooTest(unittest.TestCase):
    def test_bar(self):
        self.assertEqual(Foo.bar(self, x=32),64)



if __name__ == "__main__":
    unittest.main()
