'''

'''

# Write your code here

# Write your code here
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    m=l[0]
    for i in range(1,n):
        m=min(m,l[i]%l[0])
    print(m)