"""


"""

import numpy as np

n,k = map(int,input().split())

a = np.array([list(map(int,input().split())) for _ in range(n)])

for i in range(n-k+1):
    for j in range(n-k+1):
        print(np.min(a[i:i+k,j:j+k]),end=' ')
    print()