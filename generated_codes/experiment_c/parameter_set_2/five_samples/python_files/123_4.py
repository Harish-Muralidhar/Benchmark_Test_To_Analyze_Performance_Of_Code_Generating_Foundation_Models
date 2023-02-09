"""

"""

# Write your code here

def pairs(n,k,arr):
    arr.sort()
    i=0
    j=1
    count=0
    while(j<len(arr)):
        if(arr[j]-arr[i]==k):
            count+=1
            j+=1
        elif(arr[j]-arr[i]>k):
            i+=1
        else:
            j+=1
    return count

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    print(pairs(n,k,arr))