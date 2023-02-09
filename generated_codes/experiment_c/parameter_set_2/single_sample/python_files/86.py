'''

Constraints
1 <= t <= 5
3 <= N, M <= 8
1 <= sx, fx <= N
1 <= sy, fy <= M
0 <= height of the island <= 100

'''

import numpy as np

def jump(matrix, sx, sy, fx, fy):
    if sx == fx and sy == fy:
        return 1
    if matrix[sx][sy] == 0:
        return 0
    matrix[sx][sy] -= 1
    count = 0
    for i in range(sx-2, sx+3):
        for j in range(sy-2, sy+3):
            if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) and (abs(i-sx) == 2 or abs(j-sy) == 2):
                count += jump(matrix, i, j, fx, fy)
    matrix[sx][sy] += 1
    return count

def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        sx, sy = map(int, input().split())
        fx, fy = map(int, input().split())
        matrix = []
        for i in range(n):
            matrix.append(list(map(int, input().split())))
        print(jump(matrix, sx-1, sy-1, fx-1, fy-1))

if __name__ == '__main__':
    main()