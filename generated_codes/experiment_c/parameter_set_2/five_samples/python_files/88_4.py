"""


"""

import numpy as np

def main():
    n,m,q = map(int,input().split())
    sx,sy = map(int,input().split())
    p1 = list(map(int,input().split()))
    p2 = list(map(int,input().split()))
    t = list(map(int,input().split()))
    grid = np.zeros((n,m))
    grid[sx-1][sy-1] = 1
    for i in range(q):
        for j in range(t[i]):
            for k in range(n):
                for l in range(m):
                    if grid[k][l] == 1:
                        grid[k][l] = 0
                        if k-p1[0] >= 0:
                            grid[k-p1[0]][l] = 1
                        if l+p1[1] < m:
                            grid[k][l+p1[1]] = 1
                        if k+p2[0] < n:
                            grid[k+p2[0]][l] = 1
                        if l-p2[1] >= 0:
                            grid[k][l-p2[1]] = 1
        print(int(grid.sum()))

if __name__ == '__main__':
    main()