'''

Explanation

For the first test case, 4^4 = 256. The first 2 digits are 25, and the last 2 digits are 56.

For the second test case, 9^9 = 387420489. The first 3 digits are 387, and the last 3 digits are 489.

'''

import math

def first_last_k_digits(n, k):
    n_to_n = pow(n, n)
    n_to_n_str = str(n_to_n)
    first_k_digits = n_to_n_str[:k]
    last_k_digits = n_to_n_str[-k:]
    return first_k_digits, last_k_digits

def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        first_k_digits, last_k_digits = first_last_k_digits(n, k)
        print(first_k_digits, last_k_digits)

if __name__ == "__main__":
    main()