'''

'''

import math

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def max_gcd(a,g,x,y):
    max_gcd_val = -1
    count = 0
    for i in range(x-1,y):
        if gcd(g,a[i])>1:
            if a[i]>max_gcd_val:
                max_gcd_val = a[i]
                count = 1
            elif a[i]==max_gcd_val:
                count += 1
    return max_gcd_val, count

n,m = map(int,input().split())
a = list(map(int,input().split()))
for i in range(m):
    g,x,y = map(int,input().split())
    max_gcd_val, count = max_gcd(a,g,x,y)
    print(max_gcd_val, count)