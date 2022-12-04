import unittest
from datetime import datetime
from ExpiryDateCalculator import Calculator


class ExpiryDateCalculatorTest(unittest.TestCase):
    cal = Calculator()

    def assertExpiryDate(self, pay_date, pay_amount, real_expiry_date, last_expiry_date=None, first_pay_date=None):
        pay_date = datetime.strptime(pay_date, "%y%m%d")
        if real_expiry_date != "INVALID":
            real_expiry_date = datetime.strptime(real_expiry_date, "%y%m%d")

        if last_expiry_date:
            last_expiry_date = datetime.strptime(last_expiry_date, "%y%m%d")

        if first_pay_date:
            first_pay_date = datetime.strptime(first_pay_date, "%y%m%d")

        estimate_expiry_date = self.cal.calculateExpiryDate(pay_date, pay_amount, last_expiry_date, first_pay_date)

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

    def test_pay_100000_then_1_year(self):
        self.assertExpiryDate("230101", 100000, "240101")
        self.assertExpiryDate("240215", 100000, "250215")

    def test_pay_110000to190000_then_1_year_and_2to9_month(self):
        self.assertExpiryDate("230101", 130000, "240401")
        self.assertExpiryDate("200331", 180000, "211130")

    def test_pay_more_than_200000(self):
        self.assertExpiryDate("220101", 200000, "240101")
        self.assertExpiryDate("220101", 250000, "240601")
        self.assertExpiryDate("140130", 610000, "200229")

    def test_pay_before_expiry_date(self):
        self.assertExpiryDate("220115", 10000, "220217", last_expiry_date="220117", first_pay_date="210617")
        self.assertExpiryDate("231007", 110000, "250101", last_expiry_date="231201", first_pay_date="200401")

    def test_pay_before_expiry_date_but_first_pay_date_is_different(self):
        self.assertExpiryDate("220115", 10000, "220331", last_expiry_date="220228", first_pay_date="190331")
        self.assertExpiryDate("190615", 100000, "210228", last_expiry_date="200229", first_pay_date="190430")
