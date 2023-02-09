'''

Explanation

For 1994, it was Monday on 1st January. Hence, the output is saturday.

For 1991, it was Tuesday on 1st January. Hence, the output is tuesday.

For 2014, it was Wednesday on 1st January. Hence, the output is wednesday.

'''

import calendar

t = int(input())

for i in range(t):
    year = int(input())
    print(calendar.day_name[calendar.weekday(year, 1, 1)].lower())