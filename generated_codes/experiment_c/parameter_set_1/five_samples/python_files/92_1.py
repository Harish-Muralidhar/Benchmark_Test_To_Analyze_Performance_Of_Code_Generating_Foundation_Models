'''




'''

import numpy as np

t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    arr = np.array(list(map(int, input().split())))
    arr = np.sort(arr)

    #first check if it is possible to buy m packs at all
    if np.sum(arr[:m])%k!=0:
        print(-1)
    else:
        #if possible, now see if it is possible to buy m packs, such that the total candies are divisible by k
        for i in range(m, n):
            if np.sum(arr[:i])%k == 0:
                print(np.sum(arr[:i]))
                break
            elif i == n-1:
                print(-1)