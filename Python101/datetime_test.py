import unittest
from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta


class datetime_tests(unittest.TestCase):
    def test_date(self):
        d = date(1972, 8, 10)
        print(d)

    def test_date_today(self):
        today = date.today()
        print(today)
        print(today.day, today.month, today.year)
        print(today.weekday())
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        print(days[today.weekday()])

    def test_date_aprils_fool_day(self):
        # How many days until April Fools' Day?
        today = date.today()
        afd = date(today.year + 1, 4, 1)  # get April Fool's for the current year
        afd = afd.replace(year=today.year + 1)  # Get next year's April Fool's Day
        # Now calculate the amount of time until April Fool's Day
        time_to_afd = afd - today
        print("It's just", time_to_afd.days, "days until next April Fools' Day!")

    def test_datetime_now(self):
        # Get the current date and time
        print("The current date and time is:", datetime.now())

    def test_datetime_time(self):
        # Get the current time
        t = datetime.time(datetime.now())
        print("The current time is:", t)

    def test_datetime_strftime(self):
        now = datetime.now()
        # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
        print(now.strftime("The current year is: %Y"))  # full year with century
        print(now.strftime("%a, %d %B, %y"))  # abbreviated day, num, full month, abbreviated year
        # %c - locale's date and time, %x - locale's date, %X - locale's time
        print(now.strftime("Locale date and time: %c"))
        print(now.strftime("Locale date: %x"))
        print(now.strftime("Locale time: %X"))
        # Time Formatting
        # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
        print(now.strftime("Current time: %I:%M:%S %p"))  # 12-Hour:Minute:Second:AM
        print(now.strftime("24-hour time: %H:%M"))  # 24-Hour:Minute

    def test_time(self):
        print(time(14, 30, 45, 123456))  # hour, minute, second, microsecond

    def test_timedelta(self):
        delta = timedelta(days=5, hours=3, minutes=30)
        print("Delta:", delta)
        print("Seconds:", delta.total_seconds())
        now = datetime.now()
        print("Now:", now)
        future = now + timedelta(days=7)
        print("7 days later:", future)
        past = now - timedelta(hours=12)
        print("12 hours ago:", past)
