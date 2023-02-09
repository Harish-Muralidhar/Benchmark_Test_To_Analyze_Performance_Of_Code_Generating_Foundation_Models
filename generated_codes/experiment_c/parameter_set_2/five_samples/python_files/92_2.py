'''

'''

def candies(n,m,k,a):
    a.sort()
    if m>n:
        return -1
    if a[0]>k:
        return -1
    if a[m-1]<k:
        return -1
    sum=0
    for i in range(m):
        sum=sum+a[i]
    if sum%k==0:
        return sum
    else:
        return -1

t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    print(candies(n,m,k,a))