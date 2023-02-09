"""

"""

import numpy as np
t=int(input())
for _ in range(t):
    n=int(input())
    arr=[]
    for i in range(n):
        l=list(map(int,input().split()))
        arr.append(l)
    arr=np.array(arr)
    z=np.zeros((n,n))
    arr1=np.zeros((n,n))
    y=[]
    for i in range(n):
        if arr[i][i]==0:
            y.append(0)
        else:
            y.append(1)
    if (arr[0][0]==0):
        print(*y)
    else:
        print(-1)