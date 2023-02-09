"""

"""

#!/usr/bin/python

import sys

def z(n):
    z = 0
    while n > 0:
        n = n / 5
        z += n
    return z

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    print z(n)