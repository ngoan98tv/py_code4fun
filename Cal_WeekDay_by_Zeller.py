# This is a calculate weekday program.
# Refer to https://techtalk.vn/datepicker-front-end-web-va-cac-thuat-toan-cong-thuc-zeller-bang-javascript.html

import math

# Get input
date = input('Enter a date (dd/mm/yyyy): ')
_date = date.split('/')

# Convert input values to int
day = int(_date[0])
_month = int(_date[1])
_year = int(_date[2])

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