'''

'''

import math

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

def count_digits_in_range(n):
    if n == 0:
        return 0
    count = 0
    for i in range(1, n + 1):
        count += count_digits(i)
    return count

def count_digits_in_range_fast(n):
    if n == 0:
        return 0
    d = count_digits(n)
    p = 10 ** (d - 1)
    msd = n // p
    if msd == 1:
        return n % p + 1 + count_digits_in_range_fast(p - 1) + msd * (d - 1) * (p // 10)
    return p + msd * count_digits_in_range_fast(p - 1) + msd * (d - 1) * (p // 10)

def count_digits_in_range_fast_2(n):
    if n == 0:
        return 0
    d = count_digits(n)
    p = 10 ** (d - 1)
    msd = n // p
    if msd == 1:
        return n % p + 1 + count_digits_in_range_fast(p - 1) + msd * (d - 1) * (p // 10)
    return p + msd * count_digits_in_range_fast(p - 1) + msd * (d - 1) * (p // 10)

def count_digits_in_range_fast_3(n):
    if n == 0:
        return 0
    d = count_digits(n)
    p = 10 ** (d - 1)
    msd = n // p
    if msd == 1:
        return n % p + 1 + count