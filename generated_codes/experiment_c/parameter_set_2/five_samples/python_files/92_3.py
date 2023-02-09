'''


'''

def candies(n,m,k,arr):
    arr.sort()
    if m*k>sum(arr):
        return -1
    else:
        return sum(arr[:m])

t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    arr=list(map(int,input().split()))
    print(candies(n,m,k,arr))