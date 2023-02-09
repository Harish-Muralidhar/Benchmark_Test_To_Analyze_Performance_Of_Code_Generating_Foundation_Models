"""

"""

def get_candies(grid, n, m):
    candies = 0
    while n > 0 and m > 0:
        if n == 1:
            for i in range(m):
                candies += grid[0][i]
            break
        elif m == 1:
            for i in range(n):
                candies += grid[i][0]
            break
        else:
            min_row = min(grid[0])
            min_col = min(grid[i][0] for i in range(n))
            if min_row < min_col:
                for i in range(m):
                    candies += grid[0][i]
                grid = grid[1:]
                n -= 1
            elif min_row > min_col:
                for i in range(n):
                    candies += grid[i][0]
                for i in range(n):
                    grid[i] = grid[i][1:]
                m -= 1
            else:
                for i in range(m):
                    candies += grid[0][i]
                grid = grid[1:]
                n -= 1
    return candies

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        grid = []
        for j in range(n):
            grid.append(list(map(int, input().split())))
        print(get_candies(grid, n, m))