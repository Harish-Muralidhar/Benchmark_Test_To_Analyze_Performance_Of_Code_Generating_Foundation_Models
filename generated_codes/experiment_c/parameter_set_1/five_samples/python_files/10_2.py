"""

Explanation
In this example, one of the optimal ways of getting from 1 to 4 is:

1 -> 2 -> 4. The product of the special numbers will be 1 * 2 * 4 = 8, which is minimal.

"""

from math import prod
from sys import stdin, stdout 
from collections import deque

def main():
    n,k = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))

    ans = [0]*n
    q = deque()
    q.append(0)
    ans[0] = arr[0]
    for i in range(1,n):
        while q and (i-q[0]) > k:
            q.popleft()
        if q:
            ans[i] = ans[q[0]]*arr[i]
        q.append(i)

    stdout.write(str(ans[-1])+"\n")
    return

if __name__ == "__main__":
    main()