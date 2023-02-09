'''


'''

import numpy as np

n,k = map(int,input().split())

l = []

for i in range(n):
    l.append(list(map(int,input().split())))

#print(l)

arr = np.array(l)

#print(arr)

#print(arr[0:2,0:2])

#print(arr[0:2,0:2].sum())

for i in range(n-k+1):
    for j in range(n-k+1):
        print(arr[i:i+k,j:j+k].min(),end=" ")
    print()