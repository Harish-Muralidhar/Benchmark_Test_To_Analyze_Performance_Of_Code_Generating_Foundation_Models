"""

Solution:
"""
# cook your dish here
import numpy as np
for _ in range(int(input())):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    arr=np.array(arr)
    for _ in range(q):
        m=int(input())
        sums=np.zeros(m+1,dtype=np.int64)
        for i in range(n):
            for j in range(m,-1,-1):
                if j>=arr[i]:
                    sums[j]=sums[j]+sums[j-arr[i]]+1
        print(sums[m]%1000000009)