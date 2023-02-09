'''

Explanation:
The initial grid is:

        0 0 0
        1 1 0
        1 1 0

We press row-button 0. The grid becomes

        1 1 0
        1 1 0
        1 1 0

We press column-button 2. The grid becomes

        1 1 1
        1 1 1
        1 1 1

The final configuration is achieved.

Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.

'''

from typing import List

def printGrid(grid: List[List[int]]) -> None:
    for row in grid:
        for col in row:
            print(col, end=" ")
        print()

def printButtonPresses(rowPressed: List[int], colPressed: List[int]) -> None:
    print(len(rowPressed))
    for i in rowPressed:
        print(i, end=" ")
    print()
    print(len(colPressed))
    for i in colPressed:
        print(i, end=" ")
    print()

def pressRow(grid: List[List[int]], row: int) -> None:
    for col in range(len(grid[row])):
        grid[row][col] ^= 1

def pressColumn(grid: List[List[int]], col: int) -> None:
    for row in range(len(grid)):
        grid[row][col] ^= 1

def getButtonPresses(grid1: List[List[int]], grid2: List[List[int]]) -> None:
    rowPressed: List[int] = []
    colPressed: List[int] = []

    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            if grid1[i][j] != grid2[i][j]:
                pressRow(grid1, i)
                rowPressed.append(i)
                pressColumn(grid1, j)
                colPressed.append(j)

    printGrid(grid1)
    printButtonPresses(rowPressed, colPressed)

def main():
    t: int = int(input())

    for _ in range(t):
        n: int = int(input())
        grid1: List[List[int]] = []
        grid2: List[List[int]] = []

        for _ in range(n):
            grid1.append([int(x) for x in input().split()])

        for _ in range(n):
            grid2.append([int(x) for x in input().split()])

        getButtonPresses(grid1, grid2)

main()