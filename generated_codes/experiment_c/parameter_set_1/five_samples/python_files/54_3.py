/*
*/

T = int(input())
for _ in range(T):
    N = int(input())
    E, O = input().split()
    E = int(E)
    O = int(O)
    if E+O == N*(N+1)//2:
        arr = []
        for i in range(N):
            if i%2 == 0:
                arr.append(1)
            else:
                arr.append(2)
        print(*arr)
    else:
        print("-1")