"""

Explanation
For the first test case the expected amount of shuffles is 2 because we need to shuffle the sequence twice to get it sorted.

For the second test case the expected amount of shuffles is 1826/189.

For the third test case the expected amount of shuffles is 877318/35343.

"""

import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) / factorial(r) / factorial(n - r)

def expected_shuffles(n):
    # The expected number of shuffles is the sum of the expected number of shuffles
    # for each possible number of elements in the correct place.
    # For example, for n = 6, the expected number of shuffles is the sum of the
    # expected number of shuffles for 0 elements in the correct place, 1 element in
    # the correct place, 2 elements in the correct place, etc.
    #
    # For a given number of elements in the correct place, the expected number of
    # shuffles is the number of ways to choose those elements times the expected
    # number of shuffles for the remaining elements.
    #
    # For example, for n = 6 and 2 elements in the correct place, the expected number
    # of shuffles is the number of ways to choose 2 elements from 6, which is 6C2,
    # times the expected number of shuffles for the remaining 4 elements, which is
    # 4!.
    #
    # The expected number of shuffles for n elements is n!, so the expected number
    # of shuffles for the remaining 4 elements is 4!.
    #
    # The expected number of shuffles for n elements is n!, so the expected number
    # of shuffles for the remaining 4 elements is 4!.
    #
    # The expected