'''
Explanation:
In the first test case, all values are already at their correct positions.
In the second test case, the distance from 4 to its correct position (which is 1) is 2 which is greater than 1.

'''

import sys

def sequence_sort(a):
    correct_sequence = sorted(a)
    for index in range(len(a)):
        if abs(a[index] - correct_sequence[index]) > 1:
            return 'NO'
    return 'YES'

n = int(input())
for i in range(n):
    length = int(input())
    array = list(map(int, input().split()))
    print(sequence_sort(array))