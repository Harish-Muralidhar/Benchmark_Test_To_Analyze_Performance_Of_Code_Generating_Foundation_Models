'''

'''
import copy

n,m = list(map(int,input().split()))
sx, sy = list(map(int,input().split()))
fx,fy = list(map(int,input().split()))

a = []
dx = [1,2,-1,-2,1,2,-1,-2]
dy = [2,1,2,1,-2,-1,-2,-1]

for _ in range(n):
    a.append(list(map(int,input().split())))

#print(a)

def isSafe(i,j,n,m):
    if i >= 1 and j >= 1 and i <= n and j <= m:
        return 1
    return 0

def jump(i,j,n,m,a,visited,i1,j1):
    #print(i,j)
    if i == i1 and j == j1 and a[i-1][j-1] == 1:
        #print(i,j)
        return 1

    if not isSafe(i,j,n,m):
        return 0

    if visited[i-1][j-1] == 1 and a[i-1][j-1] > 0:
        return 0

    ans = 0
    if a[i-1][j-1] > 0:
        visited[i-1][j-1] = 1
        a[i-1][j-1] -= 1
        for k in range(8):
            ans += jump(i+dx[k],j+dy[k],n,m,a,visited,i1,j1)
        a[i-1][j-1] += 1
    return ans

visited = [[0 for _ in range(m)] for _ in range(n)]
a1 = copy.deepcopy(a)
print(jump(sx,sy,n,m,a1,visited,fx,fy))