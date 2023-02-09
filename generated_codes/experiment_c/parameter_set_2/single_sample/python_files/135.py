"""
For second query, 2 is directly connected to 3 by an edge. Hence distance 1.
For third query, 4 is connected to 3 by a path of length 3. Hence distance 3.

"""

def lca(a, b):
    if a == b:
        return a
    if a > b:
        a, b = b, a
    while a != b:
        if a == 1:
            return 1
        if a % 2 == 0:
            a = a // 2
        else:
            a = (a + 1) // 2
        if b % 2 == 0:
            b = b // 2
        else:
            b = (b + 1) // 2
    return a

def dist(a, b):
    return (a - b) // 2

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(dist(a, lca(a, b)) + dist(b, lca(a, b)))