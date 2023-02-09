'''

Explanation

In the first test case the expected number of shuffles is 2 because in the worst case we need to shuffle the sequence twice to get it sorted.

In the second test case the expected number of shuffles is 1826/189.

In the third test case the expected number of shuffles is 877318/35343.

'''

import math
import random

def bogosort(n):
    if n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return (n-1)*(bogosort(n-1)+bogosort(n-2))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        numerator = bogosort(n)
        denominator = math.factorial(n-1)
        gcd_value = gcd(numerator, denominator)
        print(str(int(numerator/gcd_value)) + "/" + str(int(denominator/gcd_value)))

if __name__ == "__main__":
    main()