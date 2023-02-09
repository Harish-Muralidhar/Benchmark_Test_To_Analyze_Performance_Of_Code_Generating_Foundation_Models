"""

Note
In the first test case, the sum is (1^1+2^1+...+10^1) mod 1000000 = 55.
In the second test case, the sum is (1^2+2^2+...+10^2) mod 1000000 = 385.
In the third test case, the sum is (1^3+2^3+...+10^3) mod 1000000 = 3025.
In the fourth test case, the sum is (1^4+2^4+...+10^4) mod 1000000 = 25333.

"""


# Code:

import math

t = int(input())

for i in range(t):
    n, k, p = map(int, input().split())
    print((sum([int(math.pow(x, k)) for x in range(1, n + 1)])) % p)