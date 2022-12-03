from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class Calculator:
    def calculateExpiryDate(self, pay_date, pay_amount):
        if pay_amount <= 0:
            return "INVALID"

        month_amount = pay_amount/10000
        return pay_date + relativedelta(months=month_amount)
