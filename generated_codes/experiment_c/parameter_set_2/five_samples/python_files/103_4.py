'''

Explanation
In the first test case, 4^4 = 256. The first two digits are 25, and the last two digits are 56.

In the second test case, 9^9 = 387420489. The first three digits are 387, and the last three digits are 489.

'''

import math

def first_last_digits(n, k):
    n_power_n = n**n
    n_power_n_str = str(n_power_n)
    first_k_digits = n_power_n_str[:k]
    last_k_digits = n_power_n_str[-k:]
    return first_k_digits, last_k_digits

def main():
    t = int(input())
    for i in range(t):
        n, k = [int(x) for x in input().split()]
        first_k_digits, last_k_digits = first_last_digits(n, k)
        print(first_k_digits, last_k_digits)

if __name__ == '__main__':
    main()