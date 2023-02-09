"""

"""

# Write your code here
import math
t = int(input())
while t>0:
    t-=1
    m, p = map(float, input().split())
    if p == 0:
        print(1000000000, 0)
    else:
        print(1000000000*(1-p**m)/(1-p), 1000000000*p**m/(1-p))