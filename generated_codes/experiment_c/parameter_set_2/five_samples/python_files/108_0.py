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

def get_prime_factors(n):
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n = n / i

    if n > 2:
        prime_factors.append(n)

    return prime_factors

def get_min_cards(n):
    if is_prime(n):
        return n
    else:
        prime_factors = get_prime_factors(n)
        return len(prime_factors)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(get_min_cards(n))

if __name__ == '__main__':
    main()