from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class Calculator:
    def calculateExpiryDate(self, pay_date, pay_amount):
        return pay_date + relativedelta(months=1)
