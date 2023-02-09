"""

Test case #1
For the array [10], possible subsets are {}, {10}, respective sums are 0, 10.

"""

def subset_sum(arr, n, s):
    if s == 0:
        return True
    if n == 0 and s != 0:
        return False
    if arr[n - 1] > s:
        return subset_sum(arr, n - 1, s)
    return subset_sum(arr, n - 1, s) or subset_sum(arr, n - 1, s - arr[n - 1])

def find_subset(arr, n):
    subset = set()
    for i in range(1, 2**n):
        s = 0
        for j in range(0, n):
            if i & (1 << j):
                s += arr[j]
        subset.add(s)
    return subset

def find_subset_sum(arr, n):
    subset = find_subset(arr, n)
    arr.sort()
    for i in range(1, 2**n):
        s = 0
        for j in range(0, n):
            if i & (1 << j):
                s += arr[j]
        if s in subset:
            subset.remove(s)
    return subset

def find_subset_sum_dp(arr, n):
    subset = find_subset(arr, n)
    arr.sort()
    subset_sum = [False] * (2**n)
    subset_sum[0] = True
    for i in range(1, 2**n):
        for j in range(0, n):
            if i & (1 << j):
                subset_sum[i] = subset_sum[i] or subset_sum[i - (1 << j)]
    for i in range(1, 2**n):
        if subset_sum[i]:
            s = 0
            for j in range(0, n):
                if i & (1 << j):
                    s += arr[j]
            if s in subset:
                subset.remove(s)