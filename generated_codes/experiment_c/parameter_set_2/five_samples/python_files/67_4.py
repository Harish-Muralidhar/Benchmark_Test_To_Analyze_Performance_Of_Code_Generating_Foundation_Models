'''

'''

import sys
sys.setrecursionlimit(10**6)

def dfs(node, parent):
    global x, y, cost
    if len(tree[node]) >= x:
        cost += y
    for child in tree[node]:
        if child != parent:
            dfs(child, node)

def add(node, parent, value):
    global cost
    cost += value * values[node]
    for child in tree[node]:
        if child != parent:
            add(child, node, value)

def solve(node, parent, values):
    global cost
    if len(values) == 0:
        return
    value = values.pop(0)
    add(node, parent, value)
    for child in tree[node]:
        if child != parent:
            solve(child, node, values)

n = int(input())
values = list(map(int, input().split()))
tree = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
q = int(input())
for _ in range(q):
    cost = 0
    m, x, y = map(int, input().split())
    values = list(map(int, input().split()))
    dfs(1, -1)
    solve(1, -1, values)
    print(cost)