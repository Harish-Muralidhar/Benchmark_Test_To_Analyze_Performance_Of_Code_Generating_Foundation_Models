"""

Explanation
In the first case, n^n = 256, so the answer is 25 and 56.
In the second case, n^n = 387420489, so the answer is 387 and 489.

"""

import math

def power(n, k):
    first_k = int(str(n ** n)[:k])
    last_k = int(str(n ** n)[-k:])
    print(first_k, last_k)

def power_2(n, k):
    n_power_n = n ** n
    first_k = n_power_n // (10 ** (math.floor(math.log(n_power_n, 10)) - k + 1))
    last_k = n_power_n % (10 ** k)
    print(first_k, last_k)

def power_3(n, k):
    n_power_n = n ** n
    first_k = n_power_n // (10 ** (math.floor(math.log(n_power_n, 10)) - k + 1))
    last_k = n_power_n % (10 ** k)
    print(first_k, last_k)

def power_4(n, k):
    n_power_n = n ** n
    first_k = n_power_n // (10 ** (math.floor(math.log(n_power_n, 10)) - k + 1))
    last_k = n_power_n % (10 ** k)
    print(first_k, last_k)

def power_5(n, k):
    n_power_n = n ** n
    first_k = n_power_n // (10 ** (math.floor(math.log(n_power_n, 10)) - k + 1))
    last_k = n_power_n % (10 ** k)
    print(first_k, last_k)

def power_6(n, k):
    n_power_n = n ** n
    first_k = n_power_n // (10