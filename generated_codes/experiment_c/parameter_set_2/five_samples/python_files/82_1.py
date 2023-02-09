'''


since the number of divisors of 2 is equal to the number of divisors of 5,
the number of divisors of 3 is equal to the number of divisors of 4,
the number of divisors of 1 is equal to the number of divisors of 3,
the number of divisors of 5 is equal to the number of divisors of 2,
the number of divisors of 4 is equal to the number of divisors of 1.

'''

from math import sqrt
from collections import defaultdict

def get_divisors(n):
    divisors = []
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

def get_combinations(n):
    combinations = defaultdict(list)
    for i in range(1, n+1):
        divisors = get_divisors(i)
        for divisor in divisors:
            combinations[divisor].append(i)
    return combinations

def get_num_combinations(n):
    combinations = get_combinations(n)
    num_combinations = 1
    for divisor in combinations:
        num_combinations *= len(combinations[divisor])
    return num_combinations

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(get_num_combinations(n) % 500009)