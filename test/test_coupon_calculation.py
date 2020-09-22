import unittest
from store import coupon_calculation as coupon


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(6.89, coupon.calculate_order(5.99, 5, 10), 2)
        self.assertAlmostEqual(6.40, coupon.calculate_order(5.50, 5, 15), 2)
        self.assertAlmostEqual(5.31, coupon.calculate_order(4.25, 5, 20), 2)
        self.assertAlmostEqual(3.80, coupon.calculate_order(7.75, 10, 10), 2)
        self.assertAlmostEqual(4.14, coupon.calculate_order(8.00, 10, 15), 2)
        self.assertAlmostEqual(5.18, coupon.calculate_order(9.10, 10, 20), 2)

    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(16.43, coupon.calculate_order(15.99, 5, 10), 2)
        self.assertAlmostEqual(26.42, coupon.calculate_order(25.50, 5, 15), 2)
        self.assertAlmostEqual(13.79, coupon.calculate_order(14.25, 5, 20), 1)
        self.assertAlmostEqual(24.88, coupon.calculate_order(27.75, 10, 10), 2)
        self.assertAlmostEqual(13.15, coupon.calculate_order(18.00, 10, 15), 1)
        self.assertAlmostEqual(24.14, coupon.calculate_order(29.10, 10, 20), 1)

    def test_price_under_between_thirty_fifty(self):
        self.assertAlmostEqual(37.51, coupon.calculate_order(35.99, 5, 10), 2)
        self.assertAlmostEqual(48.44, coupon.calculate_order(45.50, 5, 15), 2)
        self.assertAlmostEqual(32.75, coupon.calculate_order(34.25, 5, 20), 2)
        self.assertAlmostEqual(47.96, coupon.calculate_order(47.75, 10, 10), 2)
        self.assertAlmostEqual(33.17, coupon.calculate_order(38.00, 10, 15), 1)
        self.assertAlmostEqual(32.62, coupon.calculate_order(39.10, 10, 20), 1)

    def test_price_under_over_fifty(self):
        self.assertAlmostEqual(60.59, coupon.calculate_order(55.99, 5, 10), 2)
        self.assertAlmostEqual(54.51, coupon.calculate_order(65.50, 5, 15), 2)
        self.assertAlmostEqual(58.71, coupon.calculate_order(74.25, 5, 20), 1)
        self.assertAlmostEqual(57.50, coupon.calculate_order(57.75, 10, 10), 2)
        self.assertAlmostEqual(64.20, coupon.calculate_order(68.00, 10, 15), 2)
        self.assertAlmostEqual(58.59, coupon.calculate_order(79.10, 10, 20), 2)


if __name__ == '__main__':
    unittest.main()
