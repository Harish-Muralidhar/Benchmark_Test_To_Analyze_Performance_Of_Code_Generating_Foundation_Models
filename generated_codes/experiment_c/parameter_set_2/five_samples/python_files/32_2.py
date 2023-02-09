'''

'''

import datetime

t = int(input())

for i in range(t):
    year = int(input())
    print(datetime.date(year, 1, 1).strftime('%A').lower())