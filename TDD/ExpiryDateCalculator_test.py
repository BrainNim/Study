import unittest
from datetime import datetime
from ExpiryDateCalculator import Calculator


class ExpiryDateCalculatorTest(unittest.TestCase):
    cal = Calculator()

    def assertExpiryDate(self, pay_date, pay_amount, real_expiry_date):
        pay_date = datetime.strptime(pay_date, "%y%m%d")
        real_expiry_date = datetime.strptime(real_expiry_date, "%y%m%d")
        estimate_expiry_date = self.cal.calculateExpiryDate(pay_date, pay_amount)
        self.assertEqual(estimate_expiry_date, real_expiry_date)

    def test_pay_10000_then_1_month(self):
        self.assertExpiryDate("221205", 10000, "230105")
        self.assertExpiryDate("220131", 10000, "220228")
        self.assertExpiryDate("230531", 10000, "230630")

    def test_pay_10000_then_1_month_but_0229_existed(self):
        self.assertExpiryDate("200131", 10000, "200229")
        self.assertExpiryDate("200130", 10000, "200229")
        self.assertExpiryDate("200129", 10000, "200229")
        self.assertExpiryDate("240130", 10000, "240229")
        self.assertExpiryDate("240229", 10000, "240329")