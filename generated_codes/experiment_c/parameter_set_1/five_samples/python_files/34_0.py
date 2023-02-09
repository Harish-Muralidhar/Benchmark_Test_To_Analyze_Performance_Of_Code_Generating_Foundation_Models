"""

Explanation

In each separate line you have to print the second largest among A, B and C.
"""

n = int(input())
for i in range(n):
    a, b, c = sorted(map(int, input().split()))[::-1]
    print(a if a == b else b)