"""


"""

MAX = 11

def collisions(N, M, A,B):
    a = set()
    b = set()
    for i in range(N):
        a.clear()
        for j in range(M):
            if A[i][j] == 1:
                a.add(j)
        for j in range(M):
            if A[i][j] == 1:
                for k in a:
                    if k != j:
                        B[j][k] = 1

if __name__ == '__main__':
    inp = int(input())
    for i in range(inp):
        N, M = list(map(int, input().split()))
        A = [['' for i in range(M)] for j in range(N)]
        for j in range(N):
            A[j] = list(map(int, list(input())))
        B = [[0 for i in range(M)] for j in range(M)]
        collisions(N, M, A, B)
        a = 0
        for j in range(M):
            for k in range(j+1,M):
                a += B[j][k]
        print(a)