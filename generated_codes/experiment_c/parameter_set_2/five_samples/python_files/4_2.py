'''


'''

import numpy as np

def subarray_count(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i,n):
            if np.sum(arr[i:j+1]) == np.prod(arr[i:j+1]):
                count += 1
    return count

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(subarray_count(arr))