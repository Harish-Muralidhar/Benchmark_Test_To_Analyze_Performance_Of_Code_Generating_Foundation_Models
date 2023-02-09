'''

Note
This problem is inspired by the following problem.
https://www.codechef.com/problems/MINSEGM/

'''

N, K, P = map(int, input().split())
seq = [int(input()) for _ in range(N)]

def find_min_segment_sum_modulo_P(seq, K, P):
    # store the running sums
    sums = []
    sums.append(seq[0])
    for i in range(1, len(seq)):
        sums.append(seq[i] + sums[-1])
    # build the segment tree
    tree = [0] * 2 * N
    def build_segment_tree(node, start, end):
        if start == end:
            tree[node] = sums[start]
        else:
            mid = (start + end) // 2
            build_segment_tree(2 * node, start, mid)
            build_segment_tree(2 * node + 1, mid + 1, end)
            tree[node] = tree[2 * node] + tree[2 * node + 1]
    build_segment_tree(1, 0, N - 1)
    # find the minimum segment sum modulo P that is at least K
    def query(node, start, end, l, r):
        # the segment of this node is completely outside the given range
        if start > r or end < l:
            return P + 1
        # the segment of this node is completely inside the given range
        if start >= l and end <= r:
            return tree[node] % P
        # the segment of this node is partially inside and partially outside the given range
        mid = (start + end) // 2
        q1 = query(2 * node, start, mid, l, r)
        q2 = query(2 * node + 1, mid + 1, end, l, r)
        return min(q1, q2)
    ans = query(1, 0, N - 1, 0, N - 1)
    if ans >= K:
        return ans
    for i in range(N):
        for j in range(i + 1, N):
            ans = query(1, 0, N - 1, i, j)
            if ans >= K:
                return ans
    return -1

print(find_min_segment_sum_modulo_P(seq, K, P))