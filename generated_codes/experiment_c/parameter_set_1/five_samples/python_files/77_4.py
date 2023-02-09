'''

Example 3


Input:
7 9
..D$...DD
D.......D
.D.D.D..D
.D.D.D.D.
.D.D.D.D.
.D.D.D.D.
.D.D.D.D.
.D.D.D.D.
.D.D.D.D.
@.D.D.D..

Output:
1



Example 4


Input:
15 10
..........
D........$
.D.......D
..D.....DD
...D...D..
....D.D...
.....D....
@..DDD....
.....D....
....D.D...
...D...D..
..D.....DD
.D.......D
D........D
..........

Output:
0



Example 5


Input:
15 10
..........
D........$
.D.......D
..D.....DD
...D...D..
....D.D...
.....D....
@...DDD...
..DDDDD...
....D.D...
...D...D..
..D.....DD
.D.......D
D........D
..........

Output:
1

'''

import numpy as np
def get_indexes(y, x, shape):
    out = []
    for i in range(3):
        for j in range(3):
            if (i, j) in ((0, 0), (0, 2), (2, 0), (2, 2)):
                continue
            outx, outy = x+j-1, y+i-1
            if 0 <= outx < shape[1] and 0 <= outy < shape[0]:
                out.append((outy, outx))
    return out

def get_distance_from_monsters(grid, monsters_pos):
    lst = []
    for i in monsters_pos:
        lst.append(grid[i])
    return min(lst)

def get_distance_from_gold_spoon(grid, gold_spoon_pos):
    return grid[gold_spoon_pos]

def get_chef_distance(grid, chef_pos):
    return grid[chef_pos]

def get_grid(grid, pos, value):
    out = grid.copy()
    out[pos] = value
    return out

def update_grid(grid, pos):
    grid = grid.copy()
    y, x = pos
    value = grid[y, x]
    indexes = get_indexes(y, x, grid.shape)
    for index in indexes:
        if grid[index] > value + 1:
            grid = get_grid(grid, index, value+1)
    return grid


def get_initial_grid(shape):
    grid = np.full(shape, np.inf)
    return grid

def get_grid_shape(n, m):
    return (n, m)

def get_grid_position(grid, ch):
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if y == ch:
                return (i, j)

def get_grid_positions(grid, ch):
    out = []
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if y == ch:
                out.append((i, j))
    return out

def get_updated_grid(grid, new_grid, pos):
    out = new_grid
    y, x = pos
    value = grid[y, x]
    indexes = get_indexes(y, x, grid.shape)
    for index in indexes:
        if out[index] > value + 1:
            out = get_grid(out, index, value+1)
    return out

def main():
    n, m = map(int, input().split())
    grid = np.array([list(input()) for _ in range(n)])
    gold_spoon_pos = get_grid_position(grid, '$')
    monsters_pos = get_grid_positions(grid, 'D')
    chef_pos = get_grid_position(grid, '@')
    initial_grid = get_initial_grid(get_grid_shape(n, m))
    initial_grid = update_grid(initial_grid, gold_spoon_pos)
    new_grid = initial_grid
    for monster in monsters_pos:
        new_grid = get_updated_grid(initial_grid, new_grid, monster)
    minimum_distance = get_chef_distance(new_grid, chef_pos) - 1
    minimum_distance = max(minimum_distance, 0)
    print(minimum_distance)

if __name__ == "__main__":
    main()