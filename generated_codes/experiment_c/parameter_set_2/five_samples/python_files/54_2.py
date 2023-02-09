'''

'''

for _ in range(int(input())):
    n = int(input())
    e,o = map(int,input().split())
    if e%2==0 and o%2==0 and e+o==n*(n+1)//2:
        print(*([2]*(e//2) + [1]*(o//2)))
    else:
        print(-1)