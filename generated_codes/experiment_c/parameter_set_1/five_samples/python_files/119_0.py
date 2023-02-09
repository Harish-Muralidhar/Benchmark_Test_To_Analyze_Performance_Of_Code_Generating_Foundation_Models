'''


'''



# Write your code here

import math


def check(num):
    possible = False
    if num == 1:
        return 'y y y'
    if num == 2:
        return 'y y n'
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            possible = True
    if possible:
        return 'y y y'
    return 'n y y'


T = int(input())
for _ in range(T):
    N = int(input())
    print(check(N))