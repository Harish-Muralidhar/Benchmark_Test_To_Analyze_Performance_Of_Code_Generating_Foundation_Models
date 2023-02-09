'''

Input:
1
5
1 2 3 4 5

Output:
15

Example case 1. There are 15 such subarrays: A[1..1], A[2..2], A[3..3], A[4..4], A[5..5], A[1..2], A[2..3], A[3..4], A[4..5], A[1..3], A[2..4], A[3..5], A[1..4], A[2..5], A[1..5].



'''

from itertools import combinations
from math import prod

testCases = int(input())
while testCases:
    testCases -= 1
    n = int(input())
    arr = [int(x) for x in input().split()]
    c = combinations(arr, 2)
    sum_prod = 0
    for x in c:
        if sum(x) == prod(x):
            sum_prod += 1
    print(sum_prod)