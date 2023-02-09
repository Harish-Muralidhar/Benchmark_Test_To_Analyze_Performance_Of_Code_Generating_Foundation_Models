"""

"""

#code
T = int(input())
for _ in range(T):
    N = int(input())
    E,O = map(int,input().split())
    if E%2 == 0 and O%2 == 0:
        if E+O == N*(N+1)//2:
            arr = [2]*(E//2) + [1]*(O//2)
            print(*arr)
        else:
            print(-1)
    else:
        print(-1)