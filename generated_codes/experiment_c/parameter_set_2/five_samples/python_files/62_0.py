'''

Explanation
The sequence of the array after each query is given below.

1 5 2 3 4
1 5 2 3 4
1 1 2 3 4
1 1 2 3 0
1 1 0 0 0

'''

import math

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.min = None
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n
        self.root = self.constructST(0, n-1)

    def constructST(self, start, end):
        if start > end:
            return None
        if start == end:
            node = Node(start, end)
            node.min = self.arr[start]
            return node
        mid = (start + end) // 2
        node = Node(start, end)
        node.left = self.constructST(start, mid)
        node.right = self.constructST(mid+1, end)
        node.min = min(node.left.min, node.right.min)
        return node

    def getMin(self, start, end):
        if start > end or start < 0 or end > self.n-1:
            return -1
        return self.getMinUtil(self.root, start, end)

    def getMinUtil(self, root, start, end):
        if root.start == start and root.end == end:
            return root.min
        mid = (root.start + root.end) // 2
        if end <= mid:
            return self.getMinUtil(root.left, start, end)
        elif start > mid:
            return self.getMinUtil(root.right, start, end)
        else:
            return min(self.getMinUtil(root.left, start, mid), self.getMinUtil(root.right, mid+1, end))

    def update(self, index