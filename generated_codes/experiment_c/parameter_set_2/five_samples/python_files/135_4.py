'''
For second query, 2 is directly connected to 3 by an edge. Hence distance 1.
For third query, 4 is connected to 3 via 2. Hence distance 2.

'''

# Write your code here
import math

def find_depth(n):
    if n==1:
        return 0
    else:
        return int(math.log2(n))

def find_parent(n):
    if n==1:
        return 1
    else:
        return int(n/2)

def find_distance(n1,n2):
    if n1==n2:
        return 0
    else:
        depth1=find_depth(n1)
        depth2=find_depth(n2)
        if depth1==depth2:
            return depth1+find_distance(find_parent(n1),find_parent(n2))
        else:
            if depth1>depth2:
                return depth1+find_distance(n1,find_parent(n2))
            else:
                return depth2+find_distance(find_parent(n1),n2)

n=int(input())
for i in range(n):
    n1,n2=map(int,input().split())
    print(find_distance(n1,n2))