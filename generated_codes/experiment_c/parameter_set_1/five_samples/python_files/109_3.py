'''

'''

import math

def triangleTransform(n):
    if n%2==0:
        return "YES"
    else:
        return "NO"
        
t = int(input())
for i in range(0,t):
    n = int(input())
    print(triangleTransform(n))