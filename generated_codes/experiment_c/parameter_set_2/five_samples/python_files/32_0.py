/*

*/

import calendar

def day_of_the_week(year):
    return calendar.day_name[calendar.weekday(year,1,1)].lower()

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        year = int(input())
        print(day_of_the_week(year))