import unittest
from datetime import datetime
from ExpiryDateCalculator import Calculator


class ExpiryDateCalculatorTest(unittest.TestCase):
    cal = Calculator()

    def test_pay_10000_then_1_month(self):
        pay_amount = 10000

        self.assertExpiryDate("221205", pay_amount, "230105")
        self.assertExpiryDate("220131", pay_amount, "220228")
        self.assertExpiryDate("230531", pay_amount, "230630")

    def assertExpiryDate(self, pay_date, pay_amount, real_expiry_date):
        pay_date = datetime.strptime(pay_date, "%y%m%d")
        real_expiry_date = datetime.strptime(real_expiry_date, "%y%m%d")
        estimate_expiry_date = self.cal.calculateExpiryDate(pay_date, pay_amount)
        self.assertEqual(estimate_expiry_date, real_expiry_date)