'''

'''

import sys
import math

def construct_tree(n, edges):
    tree = {}
    for i in range(1, n+1):
        tree[i] = []
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])
    return tree

def get_cost(tree, node_values, m, x, y):
    cost = 0
    for i in range(m):
        if len(tree[i+1]) >= x:
            cost += node_values[i] * node_values[i+1] + y
        else:
            cost += node_values[i] * node_values[i+1]
    return cost

def get_min_cost(tree, node_values, m, x, y):
    min_cost = sys.maxsize
    for i in range(m):
        cost = 0
        for j in range(m):
            if j == i:
                continue
            if len(tree[i+1]) >= x:
                cost += node_values[j] * node_values[i+1] + y
            else:
                cost += node_values[j] * node_values[i+1]
        min_cost = min(min_cost, cost)
    return min_cost

def main():
    n = int(input())
    node_values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        edges.append(list(map(int, input().split())))
    tree = construct_tree(n, edges)
    q = int(input())
    for _ in range(q):
        m, x, y = list(map(int, input().split()))
        node_values = list(map(int, input().split()))
        print(get_min_cost(tree, node_values, m, x, y))

if __name__ == '__main__':
    main()