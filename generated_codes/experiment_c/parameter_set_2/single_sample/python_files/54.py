'''

'''

def solve(n,e,o):
    if (e+o) != (n*(n+1))/2:
        return -1
    if e%2 == 0:
        even = e/2
        odd = o/2
    else:
        even = (e-1)/2
        odd = (o+1)/2
    if even > n/2 or odd > n/2:
        return -1
    arr = [0]*n
    for i in range(even):
        arr[i] = 2
    for i in range(even,even+odd):
        arr[i] = 1
    for i in range(even+odd,n):
        arr[i] = 2
    return arr

t = int(input())
for _ in range(t):
    n = int(input())
    e,o = map(int,input().split())
    ans = solve(n,e,o)
    if ans == -1:
        print(-1)
    else:
        print(*ans)