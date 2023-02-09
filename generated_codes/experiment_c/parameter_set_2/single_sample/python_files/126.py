'''

Explanation
Example case 1. The sequence is already sorted.

Example case 2. The sequence is not sorted, and the distance between the current position of any value and its correct position in the sorted order is at most 1.

'''

import sys

def almost_sorted(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            break
        i += 1
    if i == len(arr)-1:
        return 'YES'
    j = i+1
    while j < len(arr)-1:
        if arr[j] > arr[j+1]:
            break
        j += 1
    if j == len(arr)-1:
        return 'NO'
    if arr[i] > arr[j+1]:
        return 'NO'
    if arr[j] < arr[i+1]:
        return 'NO'
    if j-i == 1:
        return 'YES'
    if j-i == 2:
        return 'YES'
    if arr[i+1] > arr[j-1]:
        return 'NO'
    if arr[j+1] < arr[i-1]:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        arr = [int(x) for x in sys.stdin.readline().split()]
        print(almost_sorted(arr))