'''


'''

# Write your code here

def getSubset(arr,n,m):
    arr.sort()
    #print(arr)
    count = 0
    for i in range(n):
        for j in range(i+1,n+1):
            #print(arr[i:j])
            if sum(arr[i:j])%m == 0:
                count += 1
    return count

t = int(input())
for _ in range(t):
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(q):
        m = int(input())
        print(getSubset(arr,n,m))