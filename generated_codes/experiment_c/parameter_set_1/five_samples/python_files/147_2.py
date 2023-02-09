'''

'''



def car(n,a):
    c=1
    for i in range(1,n):
        if a[i]<=a[i-1]:
            c+=1
    return c
        
t=int(input())
for i in range(t):
    n=int(input())
    a=map(int,input().split())
    print(car(n,a))