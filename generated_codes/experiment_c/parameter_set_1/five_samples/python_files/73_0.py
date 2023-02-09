'''

'''


# Write your code here
import math
t = int(input())
for _ in range(t):
    n = int(input())
    f = list(map(int, input().split()))
    common_ratio = f[1] // f[0]
    coeff = f[0]
    joe = []
    chef = []
    for i in range(n):
        if f[i] == coeff * common_ratio:
            chef.append(f[i])
        else:
            joe.append(f[i])
        coeff *= common_ratio
    print(' '.join(map(str, joe)))
    print(' '.join(map(str, chef)))