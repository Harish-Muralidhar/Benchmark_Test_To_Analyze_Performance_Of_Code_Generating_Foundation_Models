'''

'''

import sys
import heapq

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self, root):
        self.root = root
        self.node_list = []
        self.node_list.append(root)

    def add_node(self, node, parent):
        if parent == 0:
            self.root.children.append(node)
        else:
            self.node_list[parent-1].children.append(node)
        self.node_list.append(node)

def get_min_cost(tree, x, y, values):
    cost = 0
    for i in range(len(values)):
        node = Node(values[i])
        if i == 0:
            tree.add_node(node, 0)
        else:
            parent = heapq.heappop(tree.node_list)
            if len(parent.children) >= x:
                cost += (parent.value * node.value + y)
            else:
                cost += (parent.value * node.value)
            tree.add_node(node, parent.value)
            heapq.heappush(tree.node_list, parent)
    return cost

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    values = list(map(int, sys.stdin.readline().split()))
    root = Node(values[0])
    tree = Tree(root)
    for i in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        tree.add_node(Node(values[v-1]), u)
    q = int(sys.stdin.readline())
    for i in range(q):
        m, x, y = map(int, sys.stdin.readline().split())
        values = list(map(int, sys.stdin.readline().split()))
        print(get