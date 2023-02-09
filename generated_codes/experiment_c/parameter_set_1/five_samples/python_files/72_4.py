'''

'''

import sys
def f(n):
    if n % 4 == 0:
        return 1
    if n % 2 == 0:
        return 0
    if n == 1:
        return 0
    return 1

def good_numbers(l, r, n):
    count = 0
    for x in range(l, r+1):
        if f(x) == n:
            count += 1
            if count == n:
                return x
    return -1

t = int(input().strip())
for a0 in range(t):
    l, r, n = input().strip().split(' ')
    l, r, n = [int(l), int(r), int(n)]
    print(good_numbers(l, r, n))