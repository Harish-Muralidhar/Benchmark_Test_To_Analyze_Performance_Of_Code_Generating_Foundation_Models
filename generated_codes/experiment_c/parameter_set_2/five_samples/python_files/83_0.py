'''

Explanation

The answer is 2 because 11+16+26 = 53 and 53 mod 17 is 2.

'''

import sys

def min_segment_sum(a, k, p):
    min_sum = sys.maxsize
    for i in range(len(a)):
        for j in range(i, len(a)):
            if (sum(a[i:j+1]) % p) >= k:
                min_sum = min(min_sum, sum(a[i:j+1]) % p)
    return min_sum

def main():
    n, k, p = map(int, input().split())
    a = []
    for i in range(n):
        a.append(int(input()))
    print(min_segment_sum(a, k, p))

if __name__ == '__main__':
    main()