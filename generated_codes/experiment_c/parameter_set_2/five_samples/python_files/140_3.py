"""


"""

def ways(n):
    if n==1:
        return 1
    elif n==2:
        return 5
    else:
        return (2*ways(n-1) + 3*ways(n-2))%1000000007

t = int(input())
for i in range(t):
    n = int(input())
    print(ways(n))