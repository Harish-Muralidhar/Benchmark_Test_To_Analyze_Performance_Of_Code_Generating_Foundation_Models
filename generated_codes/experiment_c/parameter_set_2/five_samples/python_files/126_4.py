'''

Explanation

Example case 1. The input sequence is already sorted.

Example case 2. The input sequence is not sorted, but all numbers are almost at their correct position.

Example case 3. The input sequence is not sorted, and some numbers are not almost at their correct position.

'''

#code

#!/usr/bin/env python

import sys

def read_input(file):
    for line in file:
        yield line.rstrip()

input = read_input(sys.stdin)
input = [int(line) for line in input]
T = input[0]

for i in range(T):
    n = input[2*i+1]
    a = input[2*i+2:2*i+n+2]
    flag = 0
    for i in range(n-1):
        if abs(a[i]-a[i+1])>1:
            flag = 1
            break
    if flag == 1:
        print('NO')
    else:
        print('YES')