"""

"""

import math

def zeros(n):
    count = 0
    i = 5
    while (n/i>=1):
        count += int(n/i)
        i *= 5
    return int(count)

t = int(input())
for i in range(t):
    n = int(input())
    print(zeros(n))