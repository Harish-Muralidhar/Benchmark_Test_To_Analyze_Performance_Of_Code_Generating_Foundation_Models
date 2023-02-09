'''

Explanation

For the first query, the answer is the minimum of the subarray A[2], A[3], A[4], A[5] = 2.
For the second query, the assignment is performed, and the array becomes A = [1, 4, 2, 3, 4].
For the third query, the answer is the minimum of the subarray A[2], A[3], A[4], A[5] = 2.
For the fourth query, the assignment is performed, and the array becomes A = [1, 4, 2, 0, 4].
For the fifth query, the answer is the minimum of the subarray A[1], A[2], A[3] = 0.

'''

# Write your code here
import math

def build(arr,tree,start,end,node):
    if start==end:
        tree[node]=arr[start]
        return
    mid=(start+end)//2
    build(arr,tree,start,mid,2*node)
    build(arr,tree,mid+1,end,2*node+1)
    tree[node]=min(tree[2*node],tree[2*node+1])

def update(arr,tree,start,end,node,l,r,x):
    if start>end or start>r or end<l:
        return
    if start==end:
        arr[start]=arr[start]&x
        tree[node]=arr[start]
        return
    mid=(start+end)//2
    update(arr,tree,start,mid,2*node,l,r,x)
    update(arr,tree,mid+1,end,2*node+1,l,r,x)
    tree[node]=min(tree[2*node],tree[2*node+1])

def query(tree,start,end,node,l,r):
    if start>end or start>r or end<l:
        return math.inf
    if start>=l and end<=r:
        return tree[node]
    mid=(start+end)//2
    q1