'''

Explanation
For the first test case the expected amount of shuffles is 2 because we need to shuffle the whole sequence twice.

For the second test case the expected amount of shuffles is 1826/189 because we need to shuffle the whole sequence once, then fix the first and the last element and shuffle the remaining elements. The expected amount of shuffles for the remaining elements is equal to the expected amount of shuffles for the sequence of first 4 natural numbers which is equal to 1826/189.

For the third test case the expected amount of shuffles is 877318/35343 because we need to shuffle the whole sequence once, then fix the first three elements and shuffle the remaining elements. The expected amount of shuffles for the remaining elements is equal to the expected amount of shuffles for the sequence of first 7 natural numbers which is equal to 877318/35343.

'''

import math

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def find_lcm(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = lcm(ans, arr[i])
    return ans

def find_denominator(n):
    ans = 1
    for i in range(1, n + 1):
        ans = lcm(ans, i)
    return ans

def find_numerator(n):
    ans = 0
    for i in range(1, n + 1):
        ans = ans + find_denominator(n) // i
    return ans

def find_gcd(numerator, denominator):
    return gcd(numerator, denominator)

def find_fraction(numerator, denominator):
    gcd = find_gcd(numerator, denominator)
    numerator = numerator // gcd
    denominator = denominator // gcd
    return str(numerator) + "/" + str(denominator)

def find_expected