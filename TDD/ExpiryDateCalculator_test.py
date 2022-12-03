import unittest
from datetime import datetime
from ExpiryDateCalculator import Calculator


class ExpiryDateCalculatorTest(unittest.TestCase):
    cal = Calculator()

    def test_pay_10000_then_1_month(self):
        pay_amount = 10000

        pay_date = datetime.strptime("221205", "%y%m%d")
        estimate_expiriy_date = self.cal.calculateExpiryDate(pay_date, pay_amount)
        real_expiry_date = datetime.strptime("230105", "%y%m%d")
        self.assertEqual(estimate_expiriy_date, real_expiry_date)

        pay_date = datetime.strptime("220131", "%y%m%d")
        estimate_expiriy_date = self.cal.calculateExpiryDate(pay_date, pay_amount)
        real_expiry_date = datetime.strptime("220228", "%y%m%d")
        self.assertEqual(estimate_expiriy_date, real_expiry_date)

        pay_date = datetime.strptime("230531", "%y%m%d")
        estimate_expiriy_date = self.cal.calculateExpiryDate(pay_date, pay_amount)
        real_expiry_date = datetime.strptime("230630", "%y%m%d")
        self.assertEqual(estimate_expiriy_date, real_expiry_date)