'''
 */


'''
Python has built in functions for GCD and LCM.
'''

import math

t = int(input())

while t != 0:
    a, b = list(map(int, input().split()))
    gcd = math.gcd(a, b)
    lcm = (a*b)//gcd
    print(gcd, lcm)
    t = t-1