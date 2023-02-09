"""
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []


class Tree:
    def __init__(self):
        self.root = None

    def __add_node(self, node, data):
        new_node = Node(data)
        node.children.append(new_node)

    def add_node(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.__add_node(self.root, data)

    def __add_node_to_node(self, node, data, parent):
        if node.data == parent:
            self.__add_node(node, data)
        else:
            for child in node.children:
                self.__add_node_to_node(child, data, parent)

    def add_node_to_node(self, data, parent):
        if self.root.data == parent:
            self.add_node(data)
        else:
            self.__add_node_to_node(self.root, data, parent)


def get_cost_in_subtree(node, x, y):
    cost = 0
    if len(node.children) >= x:
        cost += y
    for child in node.children:
        cost += child.data * node.data
        cost += get_cost_in_subtree(child, x, y)
    return cost


def get_min_cost_to_add(node, data, x, y):
    cost = node.data * data
    if len(node.children) >= x:
        cost += y
    min_cost = cost
    for child in node.children:
        cost = child.data * data
        cost += child.data * node.data
        cost += get_cost_in_subtree(child, x, y)
        min_cost = min(min_cost, cost)
    return min_cost


def get_optimal_cost_to_add(node, data, x, y):
    cost = node.data * data
    if len(node.children) >= x:
        cost += y
    min_cost = cost
    min_node = node
    for child in node.children:
        cost = child.data * data
        cost += child.data * node.data
        cost += get_cost_in_subtree(child, x, y)
        if cost < min_cost:
            min_cost = cost
            min_node = child
    return min_node, min_cost


def tree_cost(tree, x, y):
    cost = 0
    for child in tree.root.children:
        cost += child.data * tree.root.data
        cost += get_cost_in_subtree(child, x, y)
    return cost


def get_total_cost_to_add(tree, data, x, y):
    total_cost = 0
    while data:
        node, cost = get_optimal_cost_to_add(tree.root, data.pop(0), x, y)
        total_cost += cost
        tree.add_node_to_node(data.pop(0), node.data)
    return total_cost


def main():
    n = int(input())
    node_values = [int(x) for x in input().split()]
    tree = Tree()
    for i in range(n):
        tree.add_node(node_values[i])
    for i in range(n - 1):
        parent, child = map(int, input().split())
        tree.add_node_to_node(child, parent)
    q = int(input())
    for i in range(q):
        m, x, y = map(int, input().split())
        data = [int(x) for x in input().split()]
        print(get_total_cost_to_add(tree, data, x, y))


if __name__ == '__main__':
    main()