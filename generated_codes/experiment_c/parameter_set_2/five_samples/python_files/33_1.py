'''


'''

import math

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return (a*b)//gcd(a,b)

t = int(input())

for i in range(t):
    a,b = [int(x) for x in input().split()]
    print(gcd(a,b),lcm(a,b))