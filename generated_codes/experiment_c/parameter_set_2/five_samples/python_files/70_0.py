'''

Test case #2
For the array [1,2], possible subsets are {}, {1}, {2}, {1,2}, respective sums are 0, 1, 2, 3.

'''

import math

def subset_sums(arr):
    n = len(arr)
    total_subsets = int(math.pow(2,n))
    subset_sums = []
    for i in range(total_subsets):
        subset_sum = 0
        for j in range(n):
            if i & (1 << j):
                subset_sum += arr[j]
        subset_sums.append(subset_sum)
    return subset_sums

def get_arr(subset_sums):
    arr = []
    for i in range(len(subset_sums)):
        if subset_sums[i] not in arr:
            arr.append(subset_sums[i])
    return arr

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        subset_sums = list(map(int, input().split()))
        arr = get_arr(subset_sums)
        arr.sort()
        print(*arr)

if __name__ == '__main__':
    main()