'''

Explanation
Example case 1: The sequence is already sorted, so for all positions the distance between the current position of any value and its correct position is at most 1.

Example case 2: The number 1 is at its correct position, but the number 3 is too far from its correct position.
'''

import itertools
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split(' ')))
    for i in range(1,n,2):
        if a[i-1]>a[i]:
            print("NO")
            break
    else:
        print("YES")