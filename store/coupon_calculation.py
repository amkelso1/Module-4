"""
Author:
Date:

program purpose:

"""


def calculate_order(price, cash_coupon, percent_coupon):
    cash_coupon_price = price - cash_coupon
    percent_coupon_price = cash_coupon_price - (cash_coupon_price * percent_coupon / 100)
    subtotal_tax = percent_coupon_price * 1.06

    if percent_coupon_price < 10:
        shipping = 5.95
    elif percent_coupon_price < 30:
        shipping = 7.95
    elif percent_coupon_price < 50:
        shipping = 11.95
    else:
        shipping = 0
    return subtotal_tax + shipping


if __name__ == '__main__':
    (calculate_order(47.75, 10, 10))
