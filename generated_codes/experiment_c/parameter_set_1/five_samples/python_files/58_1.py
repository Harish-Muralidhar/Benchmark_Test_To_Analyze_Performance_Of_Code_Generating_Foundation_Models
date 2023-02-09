'''

'''

# Solution

t = int(input())

while t>0:
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    M = 1<<m
    for i in range(n):
        A[i] = A[i]%M
    ans=0
    count = {}
    count[0]=1
    sum = 0
    for i in range(n):
        sum = (sum+A[i])%M
        ans = (ans+count[sum])%1000000009
        count[sum]+=1
    print(ans)
    t-=1