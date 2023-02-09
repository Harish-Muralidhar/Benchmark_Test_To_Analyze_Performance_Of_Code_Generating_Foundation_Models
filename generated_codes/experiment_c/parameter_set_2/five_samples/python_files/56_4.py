'''

'''

def kalakeyas(n,k):
    if k==0:
        return [i for i in range(1,n+1)]
    if k==n:
        return [-1]
    if k>n:
        return [-1]
    if n%k==0:
        return [-1]
    if n%(2*k)==0:
        return [-1]
    else:
        if n%k==1:
            return [i for i in range(k+1,n+1)]+[i for i in range(1,k+1)]
        else:
            return [i for i in range(k+1,n+1)]+[i for i in range(1,k+1)]+[n-k]

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    print(*kalakeyas(n,k))