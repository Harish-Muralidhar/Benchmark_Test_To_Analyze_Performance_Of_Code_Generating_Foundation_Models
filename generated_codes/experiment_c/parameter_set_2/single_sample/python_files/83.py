'''

Explanation

The minimum possible segment sum modulo 17 that is at least 2 is 11 + 16 + 26 = 53 and 53 mod 17 = 2.

'''

import sys

def min_segment_sum(n, k, p, a):
    min_sum = sys.maxsize
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += a[j]
            if sum >= k:
                min_sum = min(min_sum, sum % p)
    return min_sum

if __name__ == '__main__':
    n, k, p = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(int(input()))
    print(min_segment_sum(n, k, p, a))