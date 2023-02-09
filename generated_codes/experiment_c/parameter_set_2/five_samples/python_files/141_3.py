"""

"""

def ways(n,m):
    if n==1 or m==1:
        return n*m
    if n==2 or m==2:
        return (n*m)//2 + (n*m)%2
    return (n*m)//2 + (n*m)%2

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    print(ways(n,m))