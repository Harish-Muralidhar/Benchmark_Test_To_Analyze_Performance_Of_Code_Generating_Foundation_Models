'''

'''

import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def count_primes(x1, x2, y):
    count = 0
    for x in range(x1, x2+1):
        if is_prime(x+y):
            count += 1
    return count

def main():
    t = int(input())
    for _ in range(t):
        y, x1, x2 = [int(x) for x in input().split()]
        print(count_primes(x1, x2, y))

if __name__ == "__main__":
    main()