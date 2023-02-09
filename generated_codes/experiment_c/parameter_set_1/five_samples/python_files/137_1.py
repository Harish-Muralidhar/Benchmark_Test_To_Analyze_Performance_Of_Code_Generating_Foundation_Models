'''


'''
from math import factorial, ceil
from fractions import Fraction
from itertools import combinations


def nCk(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def main():
    t = int(input())
    while t:
        n = int(input())
        den = sum(nCk(n, j) for j in range(1, n))
        num = n * nCk(n - 1, n - 2)
        ans = Fraction(num, den)
        print(ans)
        t -= 1


if __name__ == "__main__":
    main()