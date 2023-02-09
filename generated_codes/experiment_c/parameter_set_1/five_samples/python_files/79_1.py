'''

Explanation:
For the first example, the best possible position to drop the trap is at (2,2) (number in the output will be 0).  If the trap is dropped at any other position, more bugs will be caught.

'''
n,k=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(0,n-k+1):
    for j in range(0,n-k+1):
        m=l[i][j]
        for a in range(i,i+k):
            for b in range(j,j+k):
                if(l[a][b]<m):
                    m=l[a][b]
        print(m,end=" ")
    print()
    
#using numpy
import numpy as np
n,k=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
a=np.array(l)
for i in range(0,n-k+1):
    for j in range(0,n-k+1):
        x=a[i:i+k,j:j+k]
        print(np.min(x),end=" ")
    print()