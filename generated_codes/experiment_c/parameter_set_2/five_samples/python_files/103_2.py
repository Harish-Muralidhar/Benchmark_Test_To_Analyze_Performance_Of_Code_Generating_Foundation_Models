'''

Explanation
In the first case, n^n = 256, and the first and last 2 digits are 25 and 56.
In the second case, n^n = 387420489, and the first and last 3 digits are 387 and 489.

'''

import math

def first_last_k_digits(n, k):
    n_power_n = n**n
    n_power_n_str = str(n_power_n)
    first_k_digits = n_power_n_str[:k]
    last_k_digits = n_power_n_str[-k:]
    print(first_k_digits, last_k_digits)

def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        first_last_k_digits(n, k)

if __name__ == '__main__':
    main()