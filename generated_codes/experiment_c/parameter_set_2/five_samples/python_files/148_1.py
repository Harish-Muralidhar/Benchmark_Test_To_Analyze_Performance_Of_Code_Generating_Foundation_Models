'''


'''

import math

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def gcd_list(l):
    g=l[0]
    for i in range(1,len(l)):
        g=gcd(g,l[i])
    return g

def lcm(a,b):
    return a*b//gcd(a,b)

def lcm_list(l):
    g=l[0]
    for i in range(1,len(l)):
        g=lcm(g,l[i])
    return g

def solve(l):
    g=gcd_list(l)
    if g==1:
        return -1
    lcm=lcm_list(l)
    ans=0
    for i in range(len(l)):
        ans+=(lcm//l[i])-1
    return ans

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    print(solve(l))