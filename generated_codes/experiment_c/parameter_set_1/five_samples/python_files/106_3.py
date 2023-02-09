'''


'''

class Query:
    def __init__(self, query, start, end, value):
        self.query = query
        self.start = start
        self.end = end
        self.value = value

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.N = len(arr)
        self.tree = [0] * (self.N * 4 + 1)
        self.lazy = [None] * (self.N * 4 + 1)
        self.build_tree()

    def build_tree(self, node=1, start=0, end=None):
        if end is None:
            end = self.N - 1
        if start == end:
            self.tree[node] = self.arr[start]
            return
        mid = (start + end) // 2
        self.build_tree(2 * node, start, mid)
        self.build_tree(2 * node + 1, mid + 1, end)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        if self.lazy[node] is not None:
            if self.lazy[node] == 1:
                self.tree[node] += (end - start + 1) * self.lazy[node]
            else:
                self.tree[node] *= self.lazy[node]
            if start != end:
                self.lazy[2 * node] = self.lazy[node]
                self.lazy[2 * node + 1] = self.lazy[node]
            self.lazy[node] = None
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return p1 + p2

    def update_range(self, node, start, end, l, r, val):
        if self.lazy[node] is not None:
            if self.lazy[node] == 1:
                self.tree[node] += (end - start + 1) * self.lazy[node]
            else:
                self.tree[node] *= self.lazy[node]
            if start != end:
                self.lazy[2 * node] = self.lazy[node]
                self.lazy[2 * node + 1] = self.lazy[node]
            self.lazy[node] = None
        if r < start or end < l:
            return
        if l <= start and end <= r:
            if val == 1:
                self.tree[node] += (end - start + 1) * val
            else:
                self.tree[node] *= val
            if start != end:
                self.lazy[2 * node] = val
                self.lazy[2 * node + 1] = val
            return
        mid = (start + end) // 2
        self.update_range(2 * node, start, mid, l, r, val)
        self.update_range(2 * node + 1, mid + 1, end, l, r, val)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update_point(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if start <= idx and idx <= mid:
            self.update_point(2 * node, start, mid, idx, val)
        else:
            self.update_point(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

N, Q = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 3:
        query[3] = query[3]
    queries.append(Query(*query))
st = SegmentTree(arr)
for query in queries:
    if query.query == 1:
        st.update_range(1, 0, N - 1, query.start - 1, query.end - 1, query.value)
    elif query.query == 2:
        st.update_range(1, 0, N - 1, query.start - 1, query.end - 1, query.value)
    elif query.query == 3:
        st.update_point(1, 0, N - 1, query.start - 1, query.value)
    elif query.query == 4:
        print(st.query(1, 0, N - 1, query.start - 1, query.end - 1))