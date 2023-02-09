"""

Solution:
"""
import math

def gcd(a,b):
    if(a%b==0):
        return b
    else:
        return gcd(b,a%b)

n,m = map(int,input().split())
a = list(map(int,input().split()))
for _ in range(m):
    g,x,y = map(int,input().split())
    s = []
    for i in range(x,y+1):
        if(gcd(g,a[i-1])>1):
            s.append(a[i-1])
    if(len(s)==0):
        print(-1,-1)
    else:
        new = list(set(s))
        new.sort()
        print(new[-1],s.count(new[-1]))