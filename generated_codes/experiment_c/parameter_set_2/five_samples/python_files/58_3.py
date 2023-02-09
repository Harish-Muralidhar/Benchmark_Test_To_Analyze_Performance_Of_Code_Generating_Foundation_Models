'''

'''

#code

def count_partitions(arr,n,m):
    count=0
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            k=j+i-1
            sum=0
            for l in range(j,k+1):
                sum+=arr[l]
            if sum&(1<<(m-1))==0:
                count+=1
    return count

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    print(count_partitions(arr,n,m))