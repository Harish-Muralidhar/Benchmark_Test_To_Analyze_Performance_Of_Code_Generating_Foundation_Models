'''

Explanation:

For the year 1994, it was Monday on the 1st January.
For the year 1991, it was Monday on the 1st January.
For the year 2014, it was Monday on the 1st January.

'''

import calendar

t = int(input())

while t > 0:
    year = int(input())
    print(calendar.day_name[calendar.weekday(year,1,1)].lower())
    t -= 1