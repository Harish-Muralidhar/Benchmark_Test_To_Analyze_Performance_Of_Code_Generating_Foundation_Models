'''

'''

def dist(a,b,k):
    return abs(a+b-k)

def minDist(arr,k):
    arr.sort()
    min_diff=float("inf")
    arr_length=len(arr)
    
    for i in range(arr_length-1):
        d = dist(arr[i],arr[i+1],k)
        if d>min_diff:
            break
        else:
            min_diff=d
            if min_diff==0:
                break
    count=0
    for i in range(arr_length-1):
        if arr[i]+arr[i+1]>k:
            break
        else:
            if dist(arr[i],arr[i+1],k)==min_diff:
                count+=1
    return min_diff,count

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    d,c=minDist(arr,k)
    print(d,c)