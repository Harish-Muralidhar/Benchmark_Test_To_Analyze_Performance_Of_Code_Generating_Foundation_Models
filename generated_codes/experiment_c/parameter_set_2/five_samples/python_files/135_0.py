"""
For second query, 2 is directly connected to 3 by an edge. Hence distance 1.
For third query, 4 is connected to 3 through 2 by an edge. Hence distance 2.
"""

# Write your code here

import math

def get_distance(i, j):
    if(i == j):
        return 0
    if(i > j):
        i, j = j, i
    if(i == 1):
        return int(math.log2(j))
    return get_distance(i//2, j) + 1

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        i, j = map(int, input().split())
        print(get_distance(i, j))