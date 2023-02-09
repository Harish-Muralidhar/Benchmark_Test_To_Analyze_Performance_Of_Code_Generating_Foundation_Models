'''

'''

# Write your code here
n,m = map(int,input().split())
a = list(map(int,input().split()))
for i in range(m):
    x = int(input())
    b1=0
    b2=0
    for j in range(x):
        if a[j]<a[x-1]:
            b2+=a[x-1]-a[j]
        else:
            b1+=a[j]-a[x-1]
    print(b1-b2)