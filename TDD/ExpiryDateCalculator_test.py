import unittest
from datetime import datetime
from ExpiryDateCalculator import Calculator


class ExpiryDateCalculatorTest(unittest.TestCase):
    cal = Calculator()

    def assertExpiryDate(self, pay_date, pay_amount, real_expiry_date):
        pay_date = datetime.strptime(pay_date, "%y%m%d")
        if real_expiry_date != "INVALID":
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
        self.assertExpiryDate("240130", 10000, "240229")

    def test_pay_20000to90000_then_2to9_month(self):
        self.assertExpiryDate("220131", 20000, "220331")
        self.assertExpiryDate("230531", 40000, "230930")

    def test_pay_20000to90000_then_2to9_month_but_2029_existed(self):
        self.assertExpiryDate("200112", 60000, "200712")
        self.assertExpiryDate("231031", 40000, "240229")
        self.assertExpiryDate("230530", 90000, "240229")

    def test_pay_0_or_minus_then_Invalid(self):
        self.assertExpiryDate("200112", -10000, "INVALID")
        self.assertExpiryDate("231031", 0, "INVALID")

    def test_pay_that_not_divided_by_10000_then_INVALID(self):
        self.assertExpiryDate("231031", 15000, "INVALID")
        self.assertExpiryDate("221231", 27000, "INVALID")