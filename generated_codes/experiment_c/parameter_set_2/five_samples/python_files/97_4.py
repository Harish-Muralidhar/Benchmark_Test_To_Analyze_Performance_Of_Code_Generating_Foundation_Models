'''

'''

def max_candies(grid):
    n = len(grid)
    m = len(grid[0])
    if n == 1:
        return sum(grid[0])
    if m == 1:
        return sum([grid[i][0] for i in range(n)])
    if n == 2:
        return max(sum(grid[0]), sum(grid[1]))
    if m == 2:
        return max(sum([grid[i][0] for i in range(n)]), sum([grid[i][1] for i in range(n)]))
    return max(sum(grid[0]) + max_candies([grid[i][1:] for i in range(1, n)]), sum(grid[n-1]) + max_candies([grid[i][1:] for i in range(n-1)]), sum([grid[i][0] for i in range(n)]) + max_candies([grid[i][1:] for i in range(n)]), sum([grid[i][m-1] for i in range(n)]) + max_candies([grid[i][:m-1] for i in range(n)]))

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    grid = []
    for j in range(n):
        grid.append(list(map(int, input().split())))
    print(max_candies(grid))