'''

'''

import math

def prime(a,b):
    if a == b:
        return (a+1)//2
    else:
        return math.gcd(a,b)+1

t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    print(prime(a,b))