'''

Explanation:
The initial configuration is:
0 0 0
1 1 0
1 1 0
The final configuration is:
1 1 1
1 1 1
1 1 1

One way to achieve this final configuration from the initial configuration is to press the button in the first row. The resulting configuration is:
1 1 0
1 1 0
1 1 0
The final configuration is obtained by pressing buttons in the second and third rows.

'''

import copy
import sys

sys.setrecursionlimit(5000000)


def togglerows(grid, n, r):
    for i in range(n):
        if grid[r][i] == 1:
            grid[r][i] = 0
        else:
            grid[r][i] = 1


def togglecols(grid, n, c):
    for i in range(n):
        if grid[i][c] == 1:
            grid[i][c] = 0
        else:
            grid[i][c] = 1


def check(sgrid, tgrid, n, i, j, r_list, c_list):
    if i == n:
        return True
    if j == n:
        return check(sgrid, tgrid, n, i + 1, 0, r_list, c_list)

    if sgrid[i][j] == tgrid[i][j]:
        return check(sgrid, tgrid, n, i, j + 1, r_list, c_list)

    if sgrid[i][j] != tgrid[i][j]:
        togglerows(sgrid, n, i)
        if i in r_list:
            r_list.remove(i)
        else:
            r_list.append(i)
        if check(sgrid, tgrid, n, i, j, r_list, c_list):
            return True
        togglerows(sgrid, n, i)
        if i in r_list:
            r_list.remove(i)
        else:
            r_list.append(i)

        togglecols(sgrid, n, j)
        if j in c_list:
            c_list.remove(j)
        else:
            c_list.append(j)
        if check(sgrid, tgrid, n, i, j, r_list, c_list):
            return True
        togglecols(sgrid, n, j)
        if j in c_list:
            c_list.remove(j)
        else:
            c_list.append(j)

        return False


def main():
    for _ in range(int(input())):
        n = int(input())
        sgrid = []
        tgrid = []
        r_list = []
        c_list = []

        for i in range(n):
            t = list(map(int, input().split()))
            sgrid.append(t)
        for i in range(n):
            t = list(map(int, input().split()))
            tgrid.append(t)
        # print(sgrid)
        # print(tgrid)
        if sgrid == tgrid:
            print(0)
            continue
        if check(sgrid, tgrid, n, 0, 0, r_list, c_list):
            print(len(r_list))
            for i in r_list:
                print(i, end=" ")
            print()
            print(len(c_list))
            for i in c_list:
                print(i, end=" ")
            print()
        else:
            print(-1)


if __name__ == '__main__':
    main()