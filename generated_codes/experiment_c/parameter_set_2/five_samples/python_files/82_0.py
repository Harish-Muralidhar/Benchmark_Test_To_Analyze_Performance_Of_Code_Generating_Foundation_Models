'''


since the number of divisors of 2 is equal to the number of divisors of 5,
the number of divisors of 3 is equal to the number of divisors of 4,
the number of divisors of 1 is equal to the number of divisors of 3,
the number of divisors of 5 is equal to the number of divisors of 2,
the number of divisors of 4 is equal to the number of divisors of 5.

In the third case, the number of valid combinations is 43264.

'''

# Write your code here

import math

def number_of_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                count += 1
            else:
                count += 2
    return count

def number_of_combinations(n):
    count = 0
    for i in range(1, n + 1):
        if number_of_divisors(i) == number_of_divisors(n):
            count += 1
    return count

t = int(input())
for i in range(t):
    n = int(input())
    print(number_of_combinations(n))