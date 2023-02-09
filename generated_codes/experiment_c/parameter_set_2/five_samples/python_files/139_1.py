'''

'''

def solve(n,x,a):
    a.sort()
    for i in range(n):
        if a[i] >= x:
            return i
    return -1

t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    print(solve(n,x,a))