"""


"""

import math

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)

for _ in range(int(input())):
    a,b = map(int,input().split())
    print(gcd(a,b),lcm(a,b))