"""

"""

#Solution:

import math

def trailingZeros(n):
    count = 0
    i = 5
    while (n / i >= 1):
        count += int(n / i)
        i *= 5
    return int(count)

t = int(input())
for i in range(t):
    n = int(input())
    print(trailingZeros(n))