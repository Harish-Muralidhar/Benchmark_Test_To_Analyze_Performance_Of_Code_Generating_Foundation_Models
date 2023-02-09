"""

"""
t = int(input())
while t>0:
    n = int(input())
    e,o = map(int,input().split())
    ans = []
    if n == 1 and o == 1:
        print(1)
        t -= 1
        continue
    if e%2 and o%2:
        ans += [1]*(e//2)
        ans += [2]*(o//2)
        ans += [2]
        print(*ans)
        t -= 1
        continue
    if e%2 and not o%2:
        ans += [1]*(o//2)
        ans += [2]*(e//2)
        ans += [1]
        print(*ans)
        t -= 1
        continue
    if not e%2 and o%2:
        ans += [2]*(o//2)
        ans += [1]*(e//2)
        ans += [2]
        print(*ans)
        t -= 1
        continue
    if not e%2 and not o%2:
        ans += [2]*(o//2)
        ans += [1]*(e//2)
        print(*ans)
        t -= 1
        continue