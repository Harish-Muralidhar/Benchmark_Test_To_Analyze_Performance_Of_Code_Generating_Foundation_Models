'''

Explanation
The sum of first 10 natural numbers is 55.
The sum of squares of first 10 natural numbers is 385.
The sum of cubes of first 10 natural numbers is 3025.
The sum of fourth powers of first 10 natural numbers is 25333.

'''

import sys

def sum_of_k_powers(n, k, p):
    sum = 0
    for i in range(1, n+1):
        sum += pow(i, k)
    return sum % p

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    while t > 0:
        n, k, p = map(int, sys.stdin.readline().split())
        print(sum_of_k_powers(n, k, p))
        t -= 1