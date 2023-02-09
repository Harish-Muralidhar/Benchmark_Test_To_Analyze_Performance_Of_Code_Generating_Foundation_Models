"""

Explanation

The minimum possible segment sum modulo 17 that is at least 2 is 11+16+26 = 53 and 53 mod 17 = 2.

"""

import sys

def min_segment_sum(n, k, p, arr):
    min_sum = sys.maxsize
    for i in range(n):
        for j in range(i, n):
            segment_sum = sum(arr[i:j+1])
            if segment_sum % p >= k:
                min_sum = min(min_sum, segment_sum % p)
    return min_sum

if __name__ == '__main__':
    n, k, p = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    print(min_segment_sum(n, k, p, arr))