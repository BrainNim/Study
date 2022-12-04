from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class Calculator:
    def calculateExpiryDate(self, pay_date, pay_amount):
        if pay_amount <= 0:
            return "INVALID"

        if (pay_amount % 10000) > 0:
            return "INVALID"

        month_amount = pay_amount/10000

        bonus_amount = int(month_amount / 10)*2
        month_amount += bonus_amount

        return pay_date + relativedelta(months=month_amount)
