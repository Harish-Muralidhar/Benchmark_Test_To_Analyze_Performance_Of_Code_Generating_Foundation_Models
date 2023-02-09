'''

Explanation:
The initial grid is:
0 0 0
1 1 0
1 1 0

The final grid is:
1 1 1
1 1 1
1 1 1

The first row-button press changes the first row to:
1 0 0
1 1 0
1 1 0

The second column-button press changes the second column to:
1 1 1
1 1 1
1 1 1

The total number of button presses is 2.

'''

# Write your code here
import sys

def solve(n, grid, final):
    row = 0
    col = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] != final[i][j]:
                row = row ^ 1
                break
    for j in range(n):
        for i in range(n):
            if grid[i][j] != final[i][j]:
                col = col ^ 1
                break
    if row + col == 0:
        print("0")
        return
    if row + col != n:
        print("-1")
        return
    print(row)
    for i in range(n):
        if grid[i][0] != final[i][0]:
            print(i, end=" ")
    print()
    print(col)
    for j in range(n):
        if grid[0][j] != final[0][j]:
            print(j, end=" ")
    print()

n = int(input())
for _ in range(n):
    n = int(input())
    grid = []
    final = []
    for i in range(n):
        grid.append([int(x) for x in input().split()])
    for i in range(n):
        final.append([int(x) for x in input().split()])
    solve(n, grid, final)