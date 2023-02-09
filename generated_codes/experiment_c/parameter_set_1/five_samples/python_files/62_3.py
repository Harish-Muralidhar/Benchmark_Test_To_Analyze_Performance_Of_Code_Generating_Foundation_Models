'''
1

'''
# Space Complexity : O(n)
# Time Complexity : O(n)

import math
from sys import stdin, stdout

def init_segment_tree(arr, seg_tree, l, r, idx):
    if l == r:
        seg_tree[idx] = arr[l]
        return seg_tree[idx]
    
    mid = math.floor((l + r) / 2)
    seg_tree[idx] = min(init_segment_tree(arr, seg_tree, l, mid, 2 * idx + 1), init_segment_tree(arr, seg_tree, mid + 1, r, 2 * idx + 2))
    return seg_tree[idx]

def range_query(seg_tree, qlow, qhigh, low, high, idx):
    # Total overlap
    if qlow <= low and qhigh >= high:
        return seg_tree[idx]
    
    # No overlap
    if qlow > high or qhigh < low:
        return math.inf

    # Partial overlap
    mid = math.floor((low + high) / 2)
    return min(range_query(seg_tree, qlow, qhigh, low, mid, 2 * idx + 1), range_query(seg_tree, qlow, qhigh, mid + 1, high, 2 * idx + 2))

def update_segment_tree(seg_tree, arr, low, high, idx, update_idx, update_value):
    if update_idx < low or update_idx > high:
        return
    
    if low == high:
        seg_tree[idx] = update_value
        arr[update_idx] = update_value
        return
    
    mid = math.floor((low + high) / 2)
    update_segment_tree(seg_tree, arr, low, mid, 2 * idx + 1, update_idx, update_value)
    update_segment_tree(seg_tree, arr, mid + 1, high, 2 * idx + 2, update_idx, update_value)
    seg_tree[idx] = min(seg_tree[2 * idx + 1], seg_tree[2 * idx + 2])

def main():
    N, Q = map(int, stdin.readline().rstrip().split())
    arr = list(map(int, stdin.readline().rstrip().split()))

    seg_tree = [0] * (4 * N)
    init_segment_tree(arr, seg_tree, 0, len(arr) - 1, 0)
    
    while Q:
        query = list(map(int, stdin.readline().rstrip().split()))
        if query[0] == 0:
            qlow = query[1]
            qhigh = query[2]
            print(range_query(seg_tree, qlow, qhigh, 0, len(arr) - 1, 0))
        elif query[0] == 1:
            update_idx = query[1]
            update_value = query[2] & query[3]
            update_segment_tree(seg_tree, arr, 0, len(arr) - 1, 0, update_idx, update_value)
        Q -= 1

if __name__ == '__main__':
    main()