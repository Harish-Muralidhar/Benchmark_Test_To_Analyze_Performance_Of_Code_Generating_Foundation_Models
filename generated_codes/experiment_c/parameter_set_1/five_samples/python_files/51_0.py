"""


Explanation
       

First case, you can give 100$ to everyone except employee "cmmi-8">2, who will get 140$. Second case, it is not possible to distribute the bonus among employees. 

"""

import sys
sys.setrecursionlimit(10**9)

def DFS(node):
    visited[node-1] = True
    for x in g[node-1]:
        if not visited[x[0]-1]:
            DFS(x[0])
            if ((bonus[node-1] - bonus[x[0]-1] < x[1])):
                bonus[node-1] = bonus[x[0]-1] + x[1]

def dfs_wrapper(start):
    visited = [False]*len(bonus)
    DFS(start)
    return bonus

T = int(input())
for t in range(T):
    N, M, L = list(map(int, input().split()))
    g = [[] for i in range(N)]
    bonus = [L] * N
    visited = [False] * N
    for i in range(M):
        i, j, c = list(map(int, input().split()))
        g[i-1].append([j, c])
    for i in range(1, N+1):
        if not visited[i-1]:
            bonus = dfs_wrapper(i)
    if (max(bonus) > 1000 or min(bonus) < 0):
        print("Inconsistent analysis.")
    else:
        print(sum(bonus))
        print(" ".join(list(map(str, bonus))))