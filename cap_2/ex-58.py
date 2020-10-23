# Next Day
from datetime import timedelta
from datetime import datetime

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))


t = datetime(year, month, day) + timedelta(days=1)

print("Tomorrow, will be the", (t.strftime("%Y-%m-%d")))


