"""


"""

import math
for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    gcd=arr[0]
    for i in range(1,n):
        gcd=math.gcd(gcd,arr[i])
    if k%gcd==0:
        print(0)
    else:
        print(k//gcd-1)