"""

Explanation:

1. Consider N = 3.

3! = 3 x 2 x 1 = 6

2. Consider N = 4.

4! = 4 x 3 x 2 x 1 = 24

3. Consider N = 5.

5! = 5 x 4 x 3 x 2 x 1 = 120

"""

#Solution:

import math

t = int(input())

for i in range(t):
    n = int(input())
    print(math.factorial(n))