'''

Explanation

1994 is not a leap year, so it has 365 days.

1st January 1994 is Saturday.

'''

# Write your code here

import calendar

t = int(input())

for i in range(t):
    year = int(input())
    print(calendar.day_name[calendar.weekday(year,1,1)].lower())