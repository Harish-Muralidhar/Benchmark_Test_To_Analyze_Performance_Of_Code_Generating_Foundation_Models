"""

"""

# Write your code here

def fun(n,k,arr):
    arr.sort()
    i,j=0,n-1
    min_diff=abs(arr[i]+arr[j]-k)
    count=0
    while(i<j):
        if(abs(arr[i]+arr[j]-k)<min_diff):
            min_diff=abs(arr[i]+arr[j]-k)
            count=1
        elif(abs(arr[i]+arr[j]-k)==min_diff):
            count+=1
        if(arr[i]+arr[j]>k):
            j-=1
        else:
            i+=1
    return min_diff,count

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    print(*fun(n,k,arr))