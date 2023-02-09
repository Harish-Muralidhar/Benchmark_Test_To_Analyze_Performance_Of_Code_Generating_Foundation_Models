'''

In test case 2, it is impossible to transform the triangle.

'''

import math

def is_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def is_even(n):
    return n % 2 == 0

def is_integer(n):
    return n % 1 == 0

def is_integral(n):
    return is_integer(n) and is_even(n)

def is_possible(n):
    if is_even(n):
        return True

    for i in range(2, n + 1, 2):
        if is_triangle(n, n, i):
            return True

    return False

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if is_possible(n):
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()