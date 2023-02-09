"""

Explanation:

Press the button against row 0.

Input:
1
3
0 0 0
1 1 0
1 1 0
1 1 0
1 1 1
0 0 0

Output:
-1

Explanation:

It is impossible to achieve the final configuration from the initial configuration.

"""

def solution(n, initial_grid, final_grid):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    row_presses = 0
    column_presses = 0
    row_buttons = []
    column_buttons = []
    for i in range(n):
        row_count = 0
        column_count = 0
        for j in range(n):
            if initial_grid[i][j] != final_grid[i][j]:
                row_count += 1
            if initial_grid[j][i] != final_grid[j][i]:
                column_count += 1
        if row_count % 2 != 0:
            row_presses += 1
            row_buttons.append(i)
        if column_count % 2 != 0:
            column_presses += 1
            column_buttons.append(i)
    if row_presses + column_presses > n:
        print '-1'
    else:
        print row_presses
        for i in row_buttons:
            print i,
        print
        print column_presses
        for i in column_buttons:
            print i,
        print

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        n = int(raw_input())
        initial_grid = []
        for j in range(n):
            initial_grid.append(map(int, raw_input().split()))
        final_grid = []
        for j in range(n):
            final_grid.append(map(int, raw_input().split()))
        solution(n, initial_grid, final