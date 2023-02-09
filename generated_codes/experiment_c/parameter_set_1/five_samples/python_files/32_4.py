'''


'''


import datetime
T=int(input())
i=0
while(i<T):
    year=int(input())
    if year>=1900 and year<=2500:
        x=datetime.datetime(year,1,1)
        print((x.strftime("%A")).lower())
    i=i+1