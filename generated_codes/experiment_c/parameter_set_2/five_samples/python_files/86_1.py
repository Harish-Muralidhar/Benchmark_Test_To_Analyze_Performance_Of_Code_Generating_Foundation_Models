"""


"""

import sys

def solve(n, m, sx, sy, fx, fy, heights):
    #print(n, m, sx, sy, fx, fy, heights)
    if sx < 1 or sx > n or sy < 1 or sy > m:
        return 0
    if heights[sx-1][sy-1] == 0:
        return 0
    if sx == fx and sy == fy:
        return 1
    heights[sx-1][sy-1] -= 1
    return solve(n, m, sx+1, sy, fx, fy, heights) + solve(n, m, sx+2, sy, fx, fy, heights) + solve(n, m, sx-1, sy, fx, fy, heights) + solve(n, m, sx-2, sy, fx, fy, heights) + solve(n, m, sx, sy+1, fx, fy, heights) + solve(n, m, sx, sy+2, fx, fy, heights) + solve(n, m, sx, sy-1, fx, fy, heights) + solve(n, m, sx, sy-2, fx, fy, heights)

def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        sx, sy = map(int, input().split())
        fx, fy = map(int, input().split())
        heights = []
        for j in range(n):
            heights.append(list(map(int, input().split())))
        print(solve(n, m, sx, sy, fx, fy, heights))

if __name__ == '__main__':
    main()