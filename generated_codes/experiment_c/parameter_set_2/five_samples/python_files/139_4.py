"""

"""

for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    s = sum(a)
    if s%x == 0:
        print(s//x)
    else:
        print(-1)