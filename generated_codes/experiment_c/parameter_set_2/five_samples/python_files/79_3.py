'''


'''

import numpy as np

n,k=map(int,input().split())

matrix=[]

for i in range(n):
    matrix.append(list(map(int,input().split())))

matrix=np.array(matrix)

for i in range(n-k+1):
    for j in range(n-k+1):
        print(np.min(matrix[i:i+k,j:j+k]),end=' ')
    print()