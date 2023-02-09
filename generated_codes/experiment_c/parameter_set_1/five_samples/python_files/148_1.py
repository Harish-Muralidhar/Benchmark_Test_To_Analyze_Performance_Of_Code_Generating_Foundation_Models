'''

'''

import math

def GCD(x,y):
    if(x==y):
        return x
    if(x>y):
        return GCD(x-y,y)
    return GCD(y-x,x)


def GCDFun(arr,n):
    result=arr[0]
    for i in range(1,n):
        result=GCD(arr[i],result)
    return result
    
def minballs(arr,n):
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
    if GCDFun(arr,n)==1:
        return True
    return False

def addballs(arr,n):
    for i in range(n-1):
        if arr[i]>=arr[i+1]:
            arr[i+1]=arr[i]+1
    return arr[n-1]-arr[0]+1

T=int(input("T "))
for i in range(T):
    N=int(input("N "))
    arr=list(map(int,input("array ").split()))
    if minballs(arr,N):
        print(addballs(arr,N))