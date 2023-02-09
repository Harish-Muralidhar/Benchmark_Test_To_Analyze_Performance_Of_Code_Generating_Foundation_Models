'''


Input:
1
4 5
1 2
1 1
0 0 0 0 0
2 1 3 3 3
2 3 3 3 3
1 2 3 3 3
0 0 0 0 0

Output:
3


'''
from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited = [[False]*(M+1) for m in range(N+1)]
    visited[x][y] = True
    ans = 1
    while q:
        x,y = q.popleft()
        for i,j in [(x+1,y),(x+2,y),(x-1,y),(x-2,y),(x,y+1),(x,y+2),(x,y-1),(x,y-2)]:
            if(i>0 and i <= N and j>0 and j <= M and x1[i][j]>0 and not visited[i][j]):
                q.append((i,j))
                visited[i][j] = True
                ans += 1
    return ans

t = int(input())
while t>0:
    t-=1
    N,M = map(int,input().split())
    sx,sy = map(int,input().split())
    fx,fy = map(int,input().split())
    x1 = [[0]*(M+1) for m in range(N+1)]
    for i in range(1,N+1):
        x1[i] = list(map(int,input().split()))

    ans = bfs(sx,sy)
    if(ans == N*M):
        print(0)
    else:
        print(1)