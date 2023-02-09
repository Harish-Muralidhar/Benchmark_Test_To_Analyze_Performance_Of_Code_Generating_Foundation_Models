"""

Explanation
In the first example, there are 3 possible sub-rectangles that contain even number of currants, (0,0), (1,1) and (0,0),(0,1),(1,0),(1,1).
In the second example, the possible sub-rectangles are (0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(0,3),(1,3),(0,0),(0,1),(1,0),(1,1),(0,2),(0,3),(1,2),(1,3),(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2),(0,3),(1,3),(2,3),(0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(0,2),(0,3),(1,2),(1,3),(2,2),(2,3).
"""

def f(N, M, cake):
    even = 0
    odd = 0
    for i in range(N):
        for j in range(M):
            if cake[i][j] == 1:
                odd += 1
            else:
                even += 1
    return odd, even

def g(N, M, cake):
    ans = 0
    for i in range(N):
        for j in range(M):
            for k in range(i+1, N+1):
                for l in range(j+1, M+1):
                    num = 0
                    for a in range(i, k):
                        for b in range(j, l):
                            if cake[a][b] == 1:
                                num += 1
                    if num%2==0:
                        ans += 1
    return ans

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    cake = []
    for i in range(N):
        cake.append(list(map(int, input())))
    print(g(N, M, cake))