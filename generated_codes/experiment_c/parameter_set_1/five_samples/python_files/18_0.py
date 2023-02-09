'''

'''

import math

n = int(input())

for i in range(n):
    number = int(input())
    zeros = 0
    i = 5
    while number//i > 0:
        zeros += number//i
        i *= 5
    print(zeros)