"""

Explanation

In the first test case, 100 items at 120 dollars means the total expense is 12000 dollars.

In the second test case, 10 items at 20 dollars means the total expense is 200 dollars.

In the third test case, 1200 items at 20 dollars means the total expense is 21600 dollars.

"""

#code
t = int(input())
for i in range(t):
    q,p = map(int,input().split())
    if q > 1000:
        print(q*p*0.9)
    else:
        print(q*p)