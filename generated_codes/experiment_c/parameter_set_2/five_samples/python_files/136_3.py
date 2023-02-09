"""


"""

def zombie(n,k):
    if n==1:
        return k
    else:
        return (k-1)*(zombie(n-1,k)+zombie(n-2,k))

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    print(zombie(n,k))