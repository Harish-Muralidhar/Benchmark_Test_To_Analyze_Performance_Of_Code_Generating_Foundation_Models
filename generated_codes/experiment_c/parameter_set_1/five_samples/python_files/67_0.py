"""

"""

# import sys

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.children = []
#
#
# def build_tree(N, nodes, edges):
#     root = Node(nodes[0])
#     edge_map = {x: [] for x in range(1, N+1)}
#     for edge in edges:
#         edge_map[edge[0]].append(edge[1])
#         edge_map[edge[1]].append(edge[0])
#
#     queue = [root]
#     while queue:
#         node = queue.pop(0)
#         for child_node in edge_map[node.val]:
#             child = Node(child_node)
#             node.children.append(child)
#             queue.append(child)
#
#     return root
#
#
# def get_min_cost(root, M, x, y, nodes):
#     min_cost = 0
#     i = 0
#     queue = [(root, 0)]
#     while queue:
#         node, is_child = queue.pop(0)
#         if len(node.children) >= x or is_child:
#             min_cost += (node.val * nodes[i] + y)
#             i += 1
#         if i == M or not queue:
#             break
#         for child in node.children:
#             queue.append((child, 1))
#
#     return min_cost
#
#
# N = int(sys.stdin.readline().strip())
# nodes = [int(x) for x in sys.stdin.readline().strip().split()]
# edges = [tuple([int(x) for x in sys.stdin.readline().strip().split()]) for _ in range(N-1)]
#
# root = build_tree(N, nodes, edges)
#
# Q = int(sys.stdin.readline().strip())
# for _ in range(Q):
#     M, x, y = [int(x) for x in sys.stdin.readline().strip().split()]
#     nodes = [int(x) for x in sys.stdin.readline().strip().split()]
#     print(get_min_cost(root, M, x, y, nodes))



"""

Solution #2

"""

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


def build_tree(N, nodes, edges):
    root = Node(nodes[0])
    for edge in edges:
        edge_map[edge[0]].append(edge[1])
        edge_map[edge[1]].append(edge[0])

    queue = [root]
    while queue:
        node = queue.pop(0)
        for child_node in edge_map[node.val]:
            child = Node(child_node)
            node.children.append(child)
            queue.append(child)

    return root


def get_min_cost(root, M, x, y, nodes):
    min_cost = 0
    i = 0
    queue = [(root, 0)]
    while queue:
        node, is_child = queue.pop(0)
        if len(node.children) >= x or is_child:
            min_cost += (node.val * nodes[i] + y)
            i += 1
        if i == M or not queue:
            break
        for child in node.children:
            queue.append((child, 1))

    return min_cost


N = int(sys.stdin.readline().strip())
nodes = [int(x) for x in sys.stdin.readline().strip().split()]
edges = [tuple([int(x) for x in sys.stdin.readline().strip().split()]) for _ in range(N-1)]

root = build_tree(N, nodes, edges)

Q = int(sys.stdin.readline().strip())
for _ in range(Q):
    M, x, y = [int(x) for x in sys.stdin.readline().strip().split()]
    nodes = [int(x) for x in sys.stdin.readline().strip().split()]
    print(get_min_cost(root, M, x, y, nodes))