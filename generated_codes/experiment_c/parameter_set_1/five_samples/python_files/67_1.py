"""

"""
#import the libraries
import queue

#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

#Build a tree using BFS
def buildTree():
    #Tree is built using BFS
    q = queue.Queue()
    q.put(root)
    while(q.qsize() > 0):
        curr = q.get()
        childnum = int(input("Number of children for parent " + str(curr.data) + ": "))
        for i in range(childnum):
            child = int(input("Enter the child " + str(i+1) + " of parent " + str(curr.data) + ": "))
            n = Node(child)
            curr.children.append(n)
            q.put(n)

#Function to calculate the cost
def calculateCost(root):
    q = queue.Queue()
    q.put(root)
    cost = 0
    while(q.qsize() > 0):
        curr = q.get()
        for child in curr.children:
            if(len(child.children) >= x):
                cost += (child.data * child.parent.data) + y
            else:
                cost += child.data * child.parent.data
            q.put(child)
    return cost

#Function to calculate the cost of the new Nodes
def calculateCostNewNodes(root, newNodes):
    q = queue.Queue()
    q.put(root)
    cost = 0
    while(q.qsize() > 0):
        curr = q.get()
        for child in curr.children:
            if(len(child.children) >= x):
                cost += (child.data * child.parent.data) + y
            else:
                cost += child.data * child.parent.data
            q.put(child)
    for node in newNodes:
        if(len(node.children) >= x):
            cost += (node.data * node.parent.data) + y
        else:
            cost += node.data * node.parent.data
    return cost

#Function to print the tree
def printTree(root):
    q = queue.Queue()
    q.put(root)
    while(q.qsize() > 0):
        curr = q.get()
        print("Parent " + str(curr.data))
        for child in curr.children:
            print("Child " + str(child.data))
            q.put(child)

#Main Function
def main():
    global root, x, y
    N = int(input("Enter the number of nodes in the tree: "))
    nodeValues = input("Enter the values of the nodes in the tree: ").split()
    root = Node(int(nodeValues[0]))
    for i in range(1, N):
        node = Node(int(nodeValues[i]))
        node.parent = root
        root.children.append(node)
    #buildTree()
    print("Tree built.")
    #printTree(root)
    Q = int(input("Enter the number of queries you want to perform: "))
    for i in range(Q):
        M, x, y = input("Enter the M, x, y values: ").split()
        M, x, y = int(M), int(x), int(y)
        newNodes = []
        newNodeValues = input("Enter the values of the new nodes: ").split()
        for j in range(M):
            node = Node(int(newNodeValues[j]))
            node.parent = root
            root.children.append(node)
            newNodes.append(node)
        print("The cost of adding the new nodes (from newNodes) to the tree is: " + str(calculateCostNewNodes(root, newNodes)))

main()