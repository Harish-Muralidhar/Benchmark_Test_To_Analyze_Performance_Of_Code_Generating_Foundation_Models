"""
"""

# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    for j in range(n):
        if a[j]-b[j]>=0:
            c+=1
    print(c)