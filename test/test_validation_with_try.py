import unittest
from input_validation import validation_with_try as average


class MyTestCase(unittest.TestCase):
    def test_average_negative_input(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)
    raise ValueError


if __name__ == '__main__':
    unittest.main()
