/*
*/
import math
def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

t=int(input())
while t>0:
    n=list(map(int,input().split()))
    r=n[0]
    c=n[1]
    count=0
    s=[]
    for i in range(r):
        s.append(list(input()))
    for i in range(r):
        for j in range(c):
            if s[i][j]=='#':
                continue
            L=0
            R=0
            T=0
            B=0
            k=1
            while j-k>=0 and s[i][j-k]=='^':
                L=L+1
                k=k+1
            k=1
            while j+k<c and s[i][j+k]=='^':
                R=R+1
                k=k+1
            k=1
            while i-k>=0 and s[i-k][j]=='^':
                T=T+1
                k=k+1
            k=1
            while i+k<r and s[i+k][j]=='^':
                B=B+1
                k=k+1
            #print(i,j,L,R,T,B)
            p=min(L,R,T,B)
            if L==p:
                L=L+1
            if R==p:
                R=R+1
            if T==p:
                T=T+1
            if B==p:
                B=B+1
            if isPrime(p)==True:
                count=count+1
    print(count)
    t=t-1