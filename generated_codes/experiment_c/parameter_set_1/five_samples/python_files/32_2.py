'''

'''
import calendar

num = int(input())

for i in range(num):
    year = int(input())
    print(calendar.day_name[calendar.weekday(year, 1, 1)].lower())