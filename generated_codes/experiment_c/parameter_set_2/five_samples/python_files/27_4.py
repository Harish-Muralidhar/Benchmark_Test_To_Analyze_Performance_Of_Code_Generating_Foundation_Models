'''

Explanation

In the first test case, 100 items at 120 per item, cost = 100*120 = 12000

In the second test case, 10 items at 20 per item, cost = 10*20 = 200

In the third test case, 1200 items at 20 per item, cost = 1200*20 = 24000. But as the quantity is more than 1000, 10% discount is offered. So, cost = 24000 - 24000*10/100 = 24000 - 2400 = 21600.

'''

for i in range(int(input())):
    a,b = map(int,input().split())
    if a > 1000:
        print(a*b - (a*b*10/100))
    else:
        print(a*b)