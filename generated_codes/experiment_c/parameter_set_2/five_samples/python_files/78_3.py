'''


Explanation

In the example case, the enemy battleship is located at the line segment from (-2, 2) to (1, 2). There are four guns on the ship, located at (-2, 2), (-1, 2), (0, 2), (1, 2).

However, there is a supernatural rock located at (0, 0). Therefore, you can only destroy the guns at (-2, 2) and (1, 2).

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

def count_prime_factors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0 and is_prime(i):
            count += 1
    return count

def count_guns(y, x1, x2):
    count = 0
    for i in range(x1, x2+1):
        if count_prime_factors(i) == count_prime_factors(y):
            count += 1
    return count

t = int(input())
for i in range(t):
    y, x1, x2 = map(int, input().split())
    print(count_guns(y, x1, x2))