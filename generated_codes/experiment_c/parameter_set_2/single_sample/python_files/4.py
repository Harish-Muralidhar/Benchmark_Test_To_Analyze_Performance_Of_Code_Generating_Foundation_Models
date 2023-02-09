"""


"""

import itertools

def subarray_sum_product(n, arr):
    count = 0
    for i in range(1, n+1):
        for sub in itertools.combinations(arr, i):
            if sum(sub) == reduce(lambda x, y: x*y, sub):
                count += 1
    return count

t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    arr = map(int, raw_input().split())
    print subarray_sum_product(n, arr)