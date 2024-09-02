import datetime

"""Build a script that allows you to identify the date 100 days ahead from a specified date.
For example first date 2000/01/01 the 100th day after should be 2000/04/10."""

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

day_increase = int(input("Enter the number of days that you will sum: "))


date = datetime.date(year, month, day)
new_date = date + datetime.timedelta(days=day_increase)

print(date)
print(new_date)