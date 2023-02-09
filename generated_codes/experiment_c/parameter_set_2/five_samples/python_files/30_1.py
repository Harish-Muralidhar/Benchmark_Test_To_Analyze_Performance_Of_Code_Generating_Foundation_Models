"""

Explanation

Test Case 1: Sum of angles is 180.
Test Case 2: Sum of angles is 180.
Test Case 3: Sum of angles is 180.

"""

import math

def check_triangle(a,b,c):
    if(a+b+c==180):
        return "YES"
    else:
        return "NO"

n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    print(check_triangle(a,b,c))