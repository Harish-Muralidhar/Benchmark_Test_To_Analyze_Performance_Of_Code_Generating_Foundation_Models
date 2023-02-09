'''

'''
import sys
from collections import deque

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.q = deque()
        self.parent = [None] * vertices
        self.value = [None] * vertices

    def addEdge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def get_parent(self,u):
        temp = u
        while self.parent[temp]!=None:
            temp = self.parent[temp]
        return temp

    def add_value(self,v,val):
        self.value[v] = val

    def cost(self,u,v):
        return self.value[u]*self.value[v]

    def traverse(self,v):
        self.q.append(v)
        self.parent[v] = v
        while self.q:
            u = self.q.popleft()
            for i in range(self.V):
                if self.graph[u][i] != 0 and self.parent[i] == None:
                    self.q.append(i)
                    self.parent[i] = u

    def add_node(self,u,v,val,cost):
        self.graph[u][v] = 1
        self.graph[v][u] = 1
        self.parent[v] = u
        self.value[v] = val
        if self.parent[u] != None:
            return self.cost(u,v) + cost
        else:
            return self.cost(u,v)

def main():
    N = int(input("Enter no of vertices:"))
    g = Graph(N)
    values = [int(x) for x in input("Enter the values of each vertices:").split(" ")]
    for i in range(N-1):
        u,v = [int(x) for x in input("Enter the edges:").split(" ")]
        g.addEdge(u,v)
    Q = int(input("Enter no of queries:"))
    for i in range(Q):
        M, x, y = [int(x) for x in input("Enter M,x and y:").split(" ")]
        values_added = [int(x) for x in input("Enter the values of nodes to be added:").split(" ")]
        g.traverse(0)
        cost_till_now = 0
        for i in range(M):
            min_cost = sys.maxsize
            for j in range(N):
                if g.parent[j]!=None and g.graph[j].count(1) >= x:
                    cost = g.add_node(j,N+i,values_added[i],y)
                    if cost < min_cost:
                        min_cost = cost
                        node = j
                elif g.parent[j]!=None:
                    cost = g.add_node(j,N+i,values_added[i],0)
                    if cost<min_cost:
                        min_cost = cost
                        node = j
            g.add_node(node,N+i,values_added[i],0)
            cost_till_now += min_cost
        print(cost_till_now)
        N += M
        g = Graph(N)
        for i in range(N-1):
            u,v = [int(x) for x in input("Enter the edges:").split(" ")]
            g.addEdge(u,v)
        values.extend(values_added)

if __name__ == "__main__":
    main()