"""


Input:
5 2
0 0 0 1 0
0 0 4 0 0
0 3 0 2 0
0 0 1 0 0
0 0 0 0 0

Output:
0 0 0
1 2 0
1 2 0
0 0 0



Input:
5 3
0 0 0 1 0
0 0 4 0 0
0 3 0 2 0
0 0 1 0 0
0 0 0 0 0

Output:
0 0
0 0
1 0



Input:
5 3
1 2 3 4 5
0 0 4 0 0
0 3 0 2 0
0 0 1 0 0
0 0 0 0 0

Output:
0 0
0 0
0 0

"""
import sys

try:
    n,k = map(int, raw_input().split())
    arr = [map(int, raw_input().split()) for _ in range(n)]
except:
    print("Error: Invalid Input")
    sys.exit(1)

if n > 1000 or k > n:
    print("Error: Invalid Input")
    sys.exit(1)

def find_bugs(arr, k):
    for r in range(n-k+1):
        for c in range(n-k+1):
            r1 = r
            c1 = c
            r2 = r+k
            c2 = c+k
            print min(arr[r1:r2][c1:c2]),
        print

find_bugs(arr, k)