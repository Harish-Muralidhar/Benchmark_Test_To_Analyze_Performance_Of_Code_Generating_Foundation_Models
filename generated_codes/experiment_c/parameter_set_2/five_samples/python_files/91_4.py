"""

Explanation:

The initial configuration is:

0 0 0
1 1 0
1 1 0

The final configuration is:

1 1 1
1 1 1
1 1 1

The minimum number of button presses required to transform the grid from the initial configuration to the final configuration is 2.

Press row-button 0 to get:

1 1 0
1 1 0
1 1 0

Press column-button 2 to get:

1 1 1
1 1 1
1 1 1

So, the output is:

1
0
1
2

"""

import numpy as np

def find_min_button_presses(initial_grid, final_grid):
    initial_grid = np.array(initial_grid)
    final_grid = np.array(final_grid)
    if np.array_equal(initial_grid, final_grid):
        return 0
    row_presses = 0
    col_presses = 0
    row_buttons = []
    col_buttons = []
    for i in range(initial_grid.shape[0]):
        if not np.array_equal(initial_grid[i, :], final_grid[i, :]):
            row_presses += 1
            row_buttons.append(i)
            initial_grid[i, :] = 1 - initial_grid[i, :]
    for i in range(initial_grid.shape[1]):
        if not np.array_equal(initial_grid[:, i], final_grid[:, i]):
            col_presses += 1
            col_buttons.append(i)
            initial_grid[:, i] = 1 - initial_grid[:, i]
    if np.array_equal(initial_grid, final_grid):
        return row_presses, row_buttons, col_presses, col_buttons
    else:
        return -1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        initial_grid = []
       