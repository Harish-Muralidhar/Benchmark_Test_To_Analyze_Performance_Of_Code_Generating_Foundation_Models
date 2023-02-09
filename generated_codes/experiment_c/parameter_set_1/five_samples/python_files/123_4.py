"""

"""

import numpy as np

t = int(input())

while t:
    n , k = map(int, input().split())
    a = list(map(int, input().split()))
    a = np.sort(a)
    
    ans_sum = 0
    ans_count = 0
    ans = k - a[0] - a[1]

    for i in range(n-1):
        if a[i] + a[i+1] - k < ans:
            ans = a[i] + a[i+1] - k
            ans_count = 1
        elif a[i] + a[i+1] - k == ans:
            ans_count+=1
    
    print(ans , ans_count)
    t-=1