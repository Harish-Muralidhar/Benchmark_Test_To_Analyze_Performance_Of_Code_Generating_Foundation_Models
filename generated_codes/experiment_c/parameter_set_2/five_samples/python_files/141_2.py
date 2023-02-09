"""

"""

# Write your code here

def ways(n,m):
    return (n*m*(n*m-1))//2

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    print(ways(n,m))