'''


SOLUTION:
'''
t=int(input())
while t>0:
    n,m,k=map(int,input().split())
    if n>m:
        if n-m>k:
            print(k)
        else:
            print(n-m)
    else:
        if m-n>k:
            print(k)
        else:
            print(m-n)
    t-=1