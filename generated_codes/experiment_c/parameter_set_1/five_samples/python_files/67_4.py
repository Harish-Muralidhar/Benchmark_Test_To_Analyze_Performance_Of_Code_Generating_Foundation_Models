'''


'''

import collections
from collections import defaultdict

def tree(): return defaultdict(tree)

def add(t,path):
    for node in path:
        t = t[node]
    return t

def add_node(t,node,y,x):
    b = None
    for a in t.keys():
        if len(t[a].keys()) < x:
            return t,y*node+y
    return t,0

def add_tree(t,a,b):
    t[b][a] = t[a]
    del t[a]

n = int(input())
val = list(map(int,input().split()))

t = tree()
for i in range(1,n):
    a,b = map(int,input().split())
    t[a][b] = tree()
    t[b][a] = tree()

for i in range(int(input())):
    m,x,y = map(int,input().split())
    total = 0
    node = list(map(int,input().split()))
    for j in range(m):
        for k in range(j,m):
            t,cost = add_node(t,node[k],y,x)
            total += cost
            if k==j:
                add_tree(t,node[j+1],node[j])
    print(total)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import collections
from collections import defaultdict

def tree(): return defaultdict(tree)

def add(t,path):
    for node in path:
        t = t[node]
    return t

def add_node(t,node,y,x):
    b = None
    for a in t.keys():
        if len(t[a].keys()) < x:
            return t,y*node+y
    return t,0

def add_tree(t,a,b):
    t[b][a] = t[a]
    del t[a]

n = int(input())
val = list(map(int,input().split()))

t = tree()
for i in range(1,n):
    a,b = map(int,input().split())
    t[a][b] = tree()
    t[b][a] = tree()

for i in range(int(input())):
    m,x,y = map(int,input().split())
    total = 0
    node = list(map(int,input().split()))
    for j in range(m):
        for k in range(j,m):
            t,cost = add_node(t,node[k],y,x)
            total += cost
            if k==j:
                add_tree(t,node[j+1],node[j])
    print(total)