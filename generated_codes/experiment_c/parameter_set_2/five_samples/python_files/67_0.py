"""

"""

# Solution

import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.cost = defaultdict(int)
        self.child = defaultdict(int)
        self.parent = defaultdict(int)
        self.child[1] = 0
        self.parent[1] = 0
        self.count = 0
        self.ans = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, parent):
        self.parent[node] = parent
        self.child[node] = 1
        for i in self.graph[node]:
            if i != parent:
                self.dfs(i, node)
                self.child[node] += self.child[i]

    def dfs2(self, node, parent, x, y):
        self.count += 1
        self.ans += self.cost[node]
        if self.child[node] >= x:
            self.ans += y
        for i in self.graph[node]:
            if i != parent:
                self.dfs2(i, node, x, y)

    def solve(self, x, y):
        self.dfs(1, 0)
        self.dfs2(1, 0, x, y)
        return self.ans


if __name__ == "__main__":
    n = int(input())
    g = Graph(n)
    for i in range(n-1):
        u, v = map(int, input().split())
        g.addEdge(u, v)
    for i in range(1, n+1):
        g.cost[i] = int(input())
    q = int(input())
    for i in range(q):
        m, x, y = map(int, input().split())
