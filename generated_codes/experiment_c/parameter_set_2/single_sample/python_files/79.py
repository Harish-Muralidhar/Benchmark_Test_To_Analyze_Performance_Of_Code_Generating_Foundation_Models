'''


Input:
4 3
0 1 2 3
4 5 6 7
8 9 0 1
2 3 4 0

Output:
0
0
0



Input:
4 1
0 1 2 3
4 5 6 7
8 9 0 1
2 3 4 0

Output:
0 1 2 3
4 5 6 7
8 9 0 1
2 3 4 0

'''

import numpy as np

n,k = map(int,input().split())

l = []

for i in range(n):
    l.append(list(map(int,input().split())))

l = np.array(l)

for i in range(n-k+1):
    for j in range(n-k+1):
        print(np.min(l[i:i+k,j:j+k]),end=' ')
    print()