'''

'''

#Solution

def prime(a,b):
    if a==b:
        return 2
    if a>b:
        return prime(b,a)
    if a==1:
        return 1
    return prime(a,b-a)+prime(a-1,b-1)

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print(prime(a,b))