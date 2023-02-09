'''


'''

import numpy as np
n,q=map(int,input().split())
arr=np.zeros(n)
for i in range(n):
    arr[i]=int(input().split()[i])
for i in range(q):
    query=input().split()
    q1,q2,q3,q4=map(int,query)
    if q1==1:
        arr[q2-1:q3]+=q4
    elif q1==2:
        arr[q2-1:q3]*=q4
    elif q1==3:
        arr[q2-1:q3]=q4
    else:
        print(arr[q2-1:q3].sum())