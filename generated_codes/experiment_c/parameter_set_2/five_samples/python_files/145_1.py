"""

Explanation
Example case 1.
There are no CPC in the given map.

Example case 2.
There are 3 CPC in the given map.

The first CPC is at (1, 4) with L = 3, R = 1, T = 0, B = 1. So, the minimum of [L, R, T, B] is 1. So, the prime numbers that can be accommodated are 2, 3, 5, 7. So, the number of monsters that can be accommodated is 4.

The second CPC is at (2, 8) with L = 3, R = 1, T = 1, B = 0. So, the minimum of [L, R, T, B] is 1. So, the prime numbers that can be accommodated are 2, 3, 5, 7. So, the number of monsters that can be accommodated is 4.

The third CPC is at (3, 1) with L = 0, R = 3, T = 1, B = 1. So, the minimum of [L, R, T, B] is 1. So, the prime numbers that can be accommodated are 2, 3, 5, 7. So, the number of monsters that can be accommodated is 4.

So, the total number of monsters that can be accommodated is 4 + 4 + 4 = 12.

Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.

"""

import math

def prime_cross(map, row, col):
    l = 0
    r = 0
    t = 0
    b = 0
    for i in range(col-1, -1, -1):
        if map[row][i] == '^':
            l += 1
        else:
            break
    for i in range(col+1, len(map[row])):
        if map[row][i] == '^':
            r += 1
        else:
            break
    for i in range(row-1, -1, -1):
        if map[i][col] == '^