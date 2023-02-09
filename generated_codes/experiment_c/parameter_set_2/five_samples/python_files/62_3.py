'''

Explanation

Query 1: The minimum value in the range [2, 5] is 2.
Query 2: The bitwise AND of all the elements in the range [1, 5] with 6 is 4.
Query 3: The minimum value in the range [2, 2] is 2.
Query 4: The bitwise AND of all the elements in the range [2, 5] with 3 is 0.
Query 5: The minimum value in the range [1, 3] is 1.

'''

import math

def buildTree(arr, tree, start, end, treeNode):
    if start == end:
        tree[treeNode] = arr[start]
        return
    
    mid = (start + end) // 2
    buildTree(arr, tree, start, mid, 2 * treeNode)
    buildTree(arr, tree, mid + 1, end, 2 * treeNode + 1)
    tree[treeNode] = min(tree[2 * treeNode], tree[2 * treeNode + 1])

def updateTree(arr, tree, start, end, treeNode, left, right, value):
    if start > right or end < left:
        return
    
    if start == end:
        arr[start] = arr[start] & value
        tree[treeNode] = arr[start]
        return
    
    mid = (start + end) // 2
    updateTree(arr, tree, start, mid, 2 * treeNode, left, right, value)
    updateTree(arr, tree, mid + 1, end, 2 * treeNode + 1, left, right, value)
    tree[treeNode] = min(tree[2 * treeNode], tree[2 * treeNode + 1])

def queryTree(tree, start, end, treeNode, left, right):
    if start > right or end < left:
        return math.inf
    
    if start >= left and end <= right:
        return tree[treeNode]
    
    mid = (start + end) // 2
    ans1 = queryTree(tree, start, mid, 2 * treeNode, left, right)
    ans2 = query