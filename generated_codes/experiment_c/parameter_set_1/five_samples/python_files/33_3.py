"""

"""

import math
for i in range(int(input())):
    a, b = map(int,input().split())
    gcd = math.gcd(a,b)
    lcm = (a*b)/gcd
    print(gcd, int(lcm))