'''

Explanation
In the first test case, 4^4 = 256, so the answer is 25 and 56.
In the second test case, 9^9 = 387420489, so the answer is 387 and 489.

'''

import math

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    n = n**n
    n = str(n)
    print(n[:k], n[-k:])