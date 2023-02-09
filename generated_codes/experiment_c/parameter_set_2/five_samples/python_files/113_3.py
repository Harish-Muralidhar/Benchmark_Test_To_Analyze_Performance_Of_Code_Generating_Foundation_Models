'''

'''

import math

def is_perfect_square(n):
    s = int(math.sqrt(n))
    return s*s == n

def is_fibonacci(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if is_fibonacci(n):
            print('YES')
        else:
            print('NO')