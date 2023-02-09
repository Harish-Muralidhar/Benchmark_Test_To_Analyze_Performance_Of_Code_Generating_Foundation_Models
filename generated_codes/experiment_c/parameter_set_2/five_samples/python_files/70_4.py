'''

'''

def subset_sum(arr, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if arr[n-1] > sum:
        return subset_sum(arr, n-1, sum)
    return subset_sum(arr, n-1, sum) or subset_sum(arr, n-1, sum-arr[n-1])

def find_subset(arr, n):
    subset = []
    for i in range(1, 2**n):
        sum = 0
        for j in range(0, n):
            if i & (1 << j):
                sum += arr[j]
        subset.append(sum)
    return subset

def find_array(subset, n):
    arr = []
    for i in range(1, 2**n):
        sum = 0
        for j in range(0, n):
            if i & (1 << j):
                sum += arr[j]
        subset.append(sum)
    return subset

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        subset = find_subset(arr, n)
        print(subset)
        arr = find_array(subset, n)
        print(arr)