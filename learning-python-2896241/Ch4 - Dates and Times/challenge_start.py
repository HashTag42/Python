# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

def count_days(year, month, whichday):
    # Your code goes here.
    c = calendar.TextCalendar(calendar.MONDAY)

    whichday_count = 0

    # Using https://docs.python.org/3/library/calendar.html#calendar.Calendar.itermonthdays2
    # Days returned will be tuples consisting of a day of the month number and a week day number.
    for i, day in c.itermonthdays2(year,month):
        if day == whichday:
            whichday_count += 1

    print(whichday_count)
    return whichday_count


# This is how your code will be called.
# You can edit this code to try different testing cases.
testyear = 2025
testmonth = 12
testday = 0
result = count_days(testyear, testmonth, testday)