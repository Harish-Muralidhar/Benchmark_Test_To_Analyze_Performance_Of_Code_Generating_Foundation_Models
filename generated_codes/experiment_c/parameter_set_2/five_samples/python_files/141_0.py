"""

"""

def ways(n,m):
    if n==1 or m==1:
        return max(n,m)
    else:
        return (n*m) - ((n*m)//2)

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    print(ways(n,m))