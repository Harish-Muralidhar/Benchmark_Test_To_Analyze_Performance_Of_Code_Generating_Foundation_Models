"""


"""

# Write your code here

def zombie(n,k):
    if n == 1:
        return k
    else:
        return k*zombie(n-1,k-1)

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    print(zombie(n,k))