'''

Explanation of the sample test:
The optimal way is to move from 1-st to 2-nd street, then from 2-nd to 4-th and then from 4-th to 3-rd. The product of the special numbers of these streets equals to 8.

'''

import sys
import math

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    dp = [0] * n
    dp[0] = a[0]
    for i in range(1, n):
        dp[i] = min(dp[max(0, i - k):i]) * a[i]
    print(dp[-1])

if __name__ == '__main__':
    main()