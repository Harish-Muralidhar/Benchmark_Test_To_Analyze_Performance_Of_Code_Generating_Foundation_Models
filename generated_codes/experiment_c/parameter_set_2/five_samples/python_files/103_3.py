'''

Explanation

The first test case: 42 = 16, and the first and last two digits of 16 are 2 and 6.
The second test case: 93 = 729, and the first and last three digits of 729 are 387 and 489.

'''

import math

def first_last_k_digits(n,k):
    m = str(n**n)
    return m[:k], m[-k:]

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(*first_last_k_digits(n,k))