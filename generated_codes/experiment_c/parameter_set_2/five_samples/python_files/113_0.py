'''

'''

import math

def is_fibonacci(n):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n
    return n == 0 or abs(round(a) - a) < 1.0 / n

for _ in range(int(input())):
    n = int(input())
    if is_fibonacci(n):
        print("YES")
    else:
        print("NO")