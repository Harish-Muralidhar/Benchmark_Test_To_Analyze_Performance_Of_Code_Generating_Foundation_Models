"""

Explanation

Example case 1. The only possible solution is that the Bytelandian is a Byteknight.

Example case 2. There are 5 possible solutions:

The Bytelandians are all Byteknights.
The Bytelandians are all Byteknaves.
The first Bytelandian is a Byteknight, and the rest are Byteknaves.
The first Bytelandian is a Byteknave, and the rest are Byteknights.
The first two Bytelandians are Byteknaves, and the rest are Byteknights.

Example case 3. There is only one possible solution:

The first Bytelandian is a Byteknave, and the rest are Byteknights.

"""

import sys
import math

def count_solutions(n, a, b):
    if n == 1:
        return 1
    else:
        if a[0] == 0 and b[0] == 0:
            return count_solutions(n - 1, a[1:], b[1:])
        elif a[0] == b[0]:
            return count_solutions(n - 1, a[1:], b[1:]) + count_solutions(n - 1, a[1:] + [b[0] - 1], b[1:])
        else:
            return count_solutions(n - 1, a[1:], b[1:]) + count_solutions(n - 1, a[1:] + [b[0] - 1], b[1:]) + count_solutions(n - 1, a[1:] + [a[0] + 1], b[1:])

def get_solution(n, a, b):
    if n == 1:
        return "1"
    else:
        if a[0] == 0 and b[0] == 0:
            return "0" + get_solution(n - 1, a[1:], b[1:])
        elif a[0] == b[0]:
            return "1" + get_solution(n - 1, a[1:], b[1:])
