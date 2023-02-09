'''
'''

import numpy as np

def move(grid, n, m):
    if n == 1 and m == 1:
        return grid[0][0]
    elif n == 1:
        return np.max(grid[0])
    elif m == 1:
        return np.max(grid[:,0])
    else:
        if np.sum(grid[0]) == np.sum(grid[-1]):
            return np.max(grid[0])
        elif np.sum(grid[0]) < np.sum(grid[-1]):
            return np.sum(grid[0]) + move(grid[1:,:], n-1, m)
        elif np.sum(grid[0]) > np.sum(grid[-1]):
            return np.sum(grid[-1]) + move(grid[:-1,:], n-1, m)
        else:
            if np.sum(grid[:,0]) == np.sum(grid[:,-1]):
                return np.max(grid[:,0])
            elif np.sum(grid[:,0]) < np.sum(grid[:,-1]):
                return np.sum(grid[:,0]) + move(grid[:,1:], n, m-1)
            elif np.sum(grid[:,0]) > np.sum(grid[:,-1]):
                return np.sum(grid[:,-1]) + move(grid[:,:-1], n, m-1)

# T = int(input())
# for t in range(T):
#     n,m = map(int, input().split())
#     grid = np.zeros((n,m), dtype = int)
#     for i in range(n):
#         grid[i,:] = list(map(int, input().split()))
#     print(move(grid, n, m))


def move_bob(grid, n, m):
    if n == 1 and m == 1:
        return grid[0][0]
    elif n == 1:
        return np.max(grid[0])
    elif m == 1:
        return np.max(grid[:,0])
    else:
        if np.sum(grid[0]) == np.sum(grid[-1]):
            if np.max(grid[0]) > np.max(grid[-1]):
                return np.sum(grid[0]) + move_bob(grid[1:,:], n-1, m)
            else:
                return np.sum(grid[-1]) + move_bob(grid[:-1,:], n-1, m)
        elif np.sum(grid[0]) < np.sum(grid[-1]):
            return np.sum(grid[0]) + move_bob(grid[1:,:], n-1, m)
        elif np.sum(grid[0]) > np.sum(grid[-1]):
            return np.sum(grid[-1]) + move_bob(grid[:-1,:], n-1, m)
        else:
            if np.sum(grid[:,0]) == np.sum(grid[:,-1]):
                if np.max(grid[:,0]) > np.max(grid[:,-1]):
                    return np.sum(grid[:,0]) + move_bob(grid[:,1:], n, m-1)
                else:
                    return np.sum(grid[:,-1]) + move_bob(grid[:,:-1], n, m-1)
            elif np.sum(grid[:,0]) < np.sum(grid[:,-1]):
                return np.sum(grid[:,0]) + move_bob(grid[:,1:], n, m-1)
            elif np.sum(grid[:,0]) > np.sum(grid[:,-1]):
                return np.sum(grid[:,-1]) + move_bob(grid[:,:-1], n, m-1)

T = int(input())
for t in range(T):
    n,m = map(int, input().split())
    grid = np.zeros((n,m), dtype = int)
    for i in range(n):
        grid[i,:] = list(map(int, input().split()))
    print(move_bob(grid, n, m))