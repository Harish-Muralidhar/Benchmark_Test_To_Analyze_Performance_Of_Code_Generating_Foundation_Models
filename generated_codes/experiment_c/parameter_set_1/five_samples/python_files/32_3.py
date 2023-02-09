/*

*/

import calendar

num_of_testcase = int(input())

for i in range(0,num_of_testcase):
    #year = int(input())
    year = 2001
    print(calendar.day_name[calendar.weekday(year, 1, 1)].lower())