'''

'''

# Write your code here

def check(arr,n,k):
    for i in range(n):
        if abs(arr[i]-i-1)<k:
            return False
    return True

def solve(n,k):
    arr=[i for i in range(1,n+1)]
    if check(arr,n,k):
        return arr
    else:
        for i in range(n):
            for j in range(i+1,n):
                arr[i],arr[j]=arr[j],arr[i]
                if check(arr,n,k):
                    return arr
                arr[i],arr[j]=arr[j],arr[i]
        return -1

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    ans=solve(n,k)
    if ans==-1:
        print(-1)
    else:
        print(*ans)