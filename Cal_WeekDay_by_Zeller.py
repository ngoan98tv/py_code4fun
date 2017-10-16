# Calculate weekday by Zeller formula
# Refer to https://techtalk.vn/datepicker-front-end-web-va-cac-thuat-toan-cong-thuc-zeller-bang-javascript.html

import math

# Get input
day = input('Enter the day: ')
_month = input('Enter the month: ')
_year = input('Enter the year: ')

# Save as dd/mm/yyyy to print result
date = day + '/' + _month + '/' + _year

# Convert input values to int
day = int(day)
_month = int(_month)
_year = int(_year)

# Calculate century by year
century = math.floor(_year / 100)

# Just take two last digits of year
year = _year % 100

# Get month index : month index start at March as 1 and end at February as 12
month = (_month + 10) % 12

# Execute zeller formula
zeller = ((13 * month - 1) / 5 + year / 4 + century/4 + day + year - 2 * century) % 7

# Get weekday index
_weekday = math.trunc(zeller)

# Print result
weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print("Zeller talk that: " + date + ' is ' + weekday[_weekday])
