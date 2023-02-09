'''


'''

#code

def ways(n):
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    return ways(n-1)+ways(n-2)
    
for _ in range(int(input())):
    l,r,n=map(int,input().split())
    count=0
    for i in range(l,r+1):
        if ways(i)==n:
            count+=1
            ans=i
    if count==0:
        print(-1)
    else:
        print(ans,'.'*ans)