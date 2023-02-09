'''
1

Explanation
First query is 0 2 5, so we output the minimum in the range [2, 5], which is 2.
Second query is 1 1 5 6, so we apply the assignment A[i] = A[i] & 6, for all indices i in range [1, 5].
After the assignment, array A becomes [1, 4, 2, 2, 4].
Third query is 0 2 2, so we output the minimum in the range [2, 2], which is 4.
Fourth query is 1 2 5 3, so we apply the assignment A[i] = A[i] & 3, for all indices i in range [2, 5].
After the assignment, array A becomes [1, 4, 2, 2, 0].
Fifth query is 0 1 3, so we output the minimum in the range [1, 3], which is 0.

'''

import math

def build_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build_tree(arr, tree, 2 * node, start, mid)
        build_tree(arr, tree, 2 * node + 1, mid + 1, end)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])

def update_tree(arr, tree, lazy, node, start, end, l, r, value):
    if lazy[node] != 0:
        tree[node] &= lazy[node]
        if start != end:
            lazy[2 * node] &= lazy[node]
            lazy[2 * node + 1] &= lazy[node]
        lazy[node] = 0

    if start > end or start > r or end < l:
        return

    if start >= l and end <= r:
        tree[node] &= value
        if start != end:
            lazy[2 * node] &= value
            lazy[2 * node + 1] &= value
        return

    mid = (start + end) // 2
    update_tree(arr, tree