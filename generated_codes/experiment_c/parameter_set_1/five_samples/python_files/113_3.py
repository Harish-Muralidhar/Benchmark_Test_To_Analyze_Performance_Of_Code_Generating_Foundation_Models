'''

'''

import math

def is_fib(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

def is_perfect_square(n):
    s = int(math.sqrt(n))
    return s*s == n

t = int(input())

for i in range(t):
    num = int(input())
    if is_fib(num):
        print("YES")
    else:
        print("NO")