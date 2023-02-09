'''
For second query, 2 is directly connected to 3 by an edge. Hence distance 1.
For third query, the shortest path between 4 and 3 is through the path 4->2->3. Hence distance 3.


Solution:
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def bst(a,b):
    d = abs(int(math.log(a//2,2)) - int(math.log(b//2,2)))
    return d

n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    print(bst(a,b))