"""


since the number of divisors of 1, 2 and 5 are equal to the number of divisors of 1, 3 and 5 respectively.

Remark that there are five ways to choose the first box.

In the third case, there are 43264 ways to choose the first box.

There are many test cases. Time limit is 2 seconds per test set.
"""

import math

# Returns a list of prime numbers in the range [2, N]
def sieve(N):
    p = 2
    prime = [True] * (N + 1)
    prime[1] = False
    while p**2 <= N:
        if prime[p]:
            i = p**2
            while i <= N:
                prime[i] = False
                i += p
        p += 1
    return prime


def divisors(n, primes):
    divisor_factors = []
    prime_factors = []
    # Get prime factors
    for i in range(len(primes)):
        count = 0
        while n % primes[i] == 0:
            count += 1
            n /= primes[i]
        if count > 0:
            prime_factors.append(count)
    # Get number of divisors
    for i in range(len(prime_factors)):
        divisor_factors.append(prime_factors[i] + 1)
    divisors = 1
    for i in range(len(divisor_factors)):
        divisors *= divisor_factors[i]
    return divisors


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        limit = int(math.sqrt(n))
        primes = sieve(limit)
        prime_numbers = [i for i in range(len(primes)) if primes[i]]
        prime_numbers.pop(0)
        divisors_list = []
        for i in range(1, n+1):
            divisors_list.append(divisors(i, prime_numbers))
        ans = 1
        for i in range(len(divisors_list)):
            ans *= divisors_list[i]
        # print(divisors_list)
        print(ans % 500009)