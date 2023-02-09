'''

Explanation

1994 is not a leap year, so it has 365 days. On 1st January 1994, it was Saturday.

'''

#code
import calendar

t = int(input())
for i in range(t):
    y = int(input())
    print(calendar.day_name[calendar.weekday(y, 1, 1)].lower())