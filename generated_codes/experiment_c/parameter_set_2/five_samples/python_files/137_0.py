'''

Explanation
For the first test case the expected amount of shuffles is 2. For the second test case the expected amount of shuffles is 1826/189. For the third test case the expected amount of shuffles is 877318/35343.

'''

import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)


def euler_totient(n):
    result = n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            while n % i == 0:
                n /= i
            result -= result / i
    if n > 1:
        result -= result / n
    return result


def solve(n):
    numerator = 0
    denominator = 1
    for i in range(1, n + 1):
        numerator += euler_totient(i)
        denominator *= i
    g = gcd(numerator, denominator)
    return str(numerator / g) + "/" + str(denominator / g)

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        n = int(raw_input())
        print solve(n)