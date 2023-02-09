'''

'''

import sys

def get_winner(grid):
    n = len(grid)
    m = len(grid[0])
    if n == 1:
        return sum(grid[0])
    if m == 1:
        return sum([row[0] for row in grid])

    # Alice picks row with min candies
    min_row_index = 0
    min_row_sum = sys.maxsize
    for i in range(n):
        row_sum = sum(grid[i])
        if row_sum < min_row_sum:
            min_row_sum = row_sum
            min_row_index = i

    # Bob picks column with max candies
    max_col_index = 0
    max_col_sum = 0
    for j in range(m):
        col_sum = 0
        for i in range(n):
            col_sum += grid[i][j]
        if col_sum > max_col_sum:
            max_col_sum = col_sum
            max_col_index = j

    # Remove row and column
    new_grid = []
    for i in range(n):
        if i != min_row_index:
            new_grid.append([])
            for j in range(m):
                if j != max_col_index:
                    new_grid[-1].append(grid[i][j])

    return min_row_sum + max_col_sum + get_winner(new_grid)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = [int(x) for x in input().split()]
        grid = []
        for j in range(n):
            grid.append([int(x) for x in input().split()])
        print(get_winner(grid))