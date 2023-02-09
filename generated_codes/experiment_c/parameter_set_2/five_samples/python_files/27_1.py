'''

Explanation

In the first test case, 100 items at 120 per item.
In the second test case, 10 items at 20 per item.
In the third test case, 1200 items at 20 per item.

'''

t = int(input())

for i in range(t):
    a = list(map(int,input().split()))
    if a[0] > 1000:
        print(a[0]*a[1]*0.9)
    else:
        print(a[0]*a[1])