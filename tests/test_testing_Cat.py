import testing.Cat
from testing.Cat import Cat
import unittest


class CatTest(unittest.TestCase):
    def test_calculate_cat_human_years(self):
        self.assertEqual(
            Cat.calculate_cat_human_years(self,x=5),
            35
        )


if __name__ == "__main__":
    unittest.main()
