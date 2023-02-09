'''

Test cases

1.
Input:

4 3 1 4
1 3 5
3 3 4
2 2 1
2 1 2

Output:

2


2.
Input:

3 2 2 3
1 2 3
2 2 4
1 1 1

Output:

3


3.
Input:

10 8 2 4
1 1 1
1 8 1
10 1 1
10 8 1

Output:

0



'''

def solve(w, h, d, n, barriers):
    # Write your code here
    cost = 0
    # Initializing the grid
    grid = [[0 for _ in range(w)] for _ in range(h)]
    # Marking the barriers
    for barrier in barriers:
        grid[barrier[0]][barrier[1]] = barrier[2]
    # Checking for the grid coordinates which are to be removed
    for i in range(w):
        for j in range(h):
            if (i - d) ** 2 + (j - d) ** 2 <= d ** 2:
                cost += grid[i][j]
    return cost


# Write your code here
w, h, d, n = map(int, input().split())
barriers = []
for _ in range(n):
    barriers.append(list(map(int, input().split())))
out_ = solve(w, h, d, n, barriers)
print (out_)