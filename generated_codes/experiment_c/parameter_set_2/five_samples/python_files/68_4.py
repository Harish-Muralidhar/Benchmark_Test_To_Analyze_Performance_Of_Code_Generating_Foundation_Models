'''

'''

#Solution

# cook your dish here
import math
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def ncr(n,r):
    return fact(n)/(fact(r)*fact(n-r))
t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(q):
        m=int(input())
        count=0
        for i in range(n+1):
            if ncr(n,i)%m==0:
                count+=1
        print(count)