"""


"""

import math
def query1(n,m):
    for i in range(m[0],m[1]+1):
        a[i]+=m[2]
        a[i]=a[i]%mod

def query2(n,m):
    for i in range(m[0],m[1]+1):
        a[i]*=m[2]
        a[i]=a[i]%mod

def query3(n,m):
    for i in range(m[0],m[1]+1):
        a[i]=m[2]
        
def query4(n,m):
    s=0
    for i in range(m[0],m[1]+1):
        s+=a[i]
    return(s%mod)

mod=int(math.pow(10,9)+7)
n,q=map(int,input().split())
a=list(map(int,input().split()))
for _ in range(q):
    m=list(map(int,input().split()))
    if m[0]==1:
        query1(n,m)
    elif m[0]==2:
        query2(n,m)
    elif m[0]==3:
        query3(n,m)
    elif m[0]==4:
        print(query4(n,m))