'''


'''

import math

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def is_possible(a, b, c):
    if a == b and a == c:
        return "YES"
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        return "YES"
    if a % 2 == 0 and b % 2 == 0 and c % 2 != 0:
        if is_triangle(a, b, c + 1):
            return "YES"
        if is_triangle(a, b, c - 1):
            return "YES"
    if a % 2 == 0 and b % 2 != 0 and c % 2 == 0:
        if is_triangle(a, b + 1, c):
            return "YES"
        if is_triangle(a, b - 1, c):
            return "YES"
    if a % 2 != 0 and b % 2 == 0 and c % 2 == 0:
        if is_triangle(a + 1, b, c):
            return "YES"
        if is_triangle(a - 1, b, c):
            return "YES"
    if a % 2 == 0 and b % 2 != 0 and c % 2 != 0:
        if is_triangle(a, b + 1, c + 1):
            return "YES"
        if is_triangle(a, b + 1, c - 1):
            return "YES"
        if is_triangle(a, b - 1, c + 1):
            return "YES"
        if is_triangle(a, b - 1, c - 1):
            return "YES"
    if a % 2 != 0 and b % 2 == 0 and c % 2 != 0:
        if is_triangle(a + 1, b, c + 1):
            return "YES"
        if is_triangle(a + 1, b, c - 1):
            return "YES"
        if is_tri