"""

Explanation

Example case 1. The sequence is already sorted, so the answer is YES.

Example case 2. The sequence is not sorted, so the answer is NO.

"""

import sys

def check_almost_sorted(n, a):
    count = 0
    for i in range(n):
        if abs(a[i] - i) > 1:
            count += 1
    if count > 1:
        return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(check_almost_sorted(n, a))