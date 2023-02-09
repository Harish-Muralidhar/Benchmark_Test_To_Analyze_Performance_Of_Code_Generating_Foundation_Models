"""

Explanation
Example case 1. The map is as follows:

#^^^^^#^##
^^^^^^^^^^
^^^^^^^^^#

There are no CPCs in this map.

Example case 2. The map is as follows:

^^^^#^^^^#
^^^^^^^^#^
^^##^^#^^^
#^^^^^^^#^
^^#^^^^^^^
^^^^#^^^^^
^^^^^^^^^^

There are 3 CPCs in this map.

The first CPC is at (1, 5) and can accommodate 1 monster.
The second CPC is at (2, 10) and can accommodate 2 monsters.
The third CPC is at (3, 2) and can accommodate 1 monster.

So, the answer is 1 + 2 + 1 = 4.

"""

import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_count(n):
    count = 0
    for i in range(1, n + 1):
        if is_prime(i):
            count += 1
    return count

def get_prime_cross_count(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '^':
                l = 0
                r = 0
                t = 0
                b = 0
                for k in range(j - 1, -1, -1):
                    if matrix[i][k] == '^':
                        l += 1
                    else:
                        break
                for k in range(j + 1, cols):
                    if matrix[i][k] == '^':
                        r += 1
                    else:
                        break
                for k in range(i - 1, -1, -1):
                    if matrix[k][j] == '^':
                        t += 1
                    else:
                        break