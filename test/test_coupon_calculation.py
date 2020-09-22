import unittest
from store import coupon_calculation as coupon


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(7.84, coupon.calculate_order(5.55, 5, 10),)
        self.assertAlmostEqual(6.84, coupon.calculate_order(5.99, 5, 15),)
        self.assertAlmostEqual(8.24, coupon.calculate_order(6.89, 5, 20),)
        self.assertAlmostEqual(4.50, coupon.calculate_order(2.56, 10, 10))


if __name__ == '__main__':
    unittest.main()
