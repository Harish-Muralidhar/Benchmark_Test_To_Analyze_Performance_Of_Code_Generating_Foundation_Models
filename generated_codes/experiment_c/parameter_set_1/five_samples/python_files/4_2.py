'''

'''

import itertools as it

t = int(input())

for i in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    ans = 0

    for j in range(n+1):
        sub_ar = list(it.combinations(A, j))
        for k in sub_ar:
            if sum(k) == 1:
                continue
            else:
                if sum(k) == 1 * k[0]**(j-1):
                    ans += 1
    print(ans)