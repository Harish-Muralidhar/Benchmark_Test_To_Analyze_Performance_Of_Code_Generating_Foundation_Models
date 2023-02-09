"""

"""

#Solution:

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    l=[]
    for j in range(n):
        l.append(arr[j])
        if arr[j]<min(l):
            l.remove(arr[j])
    print(sum(l))