"""

"""

def get_winner_candies(grid):
    # Write your code here
    n = len(grid)
    m = len(grid[0])
    alice_candies = 0
    bob_candies = 0
    while n > 0 and m > 0:
        if n == 1:
            alice_candies += sum(grid[0])
            break
        elif m == 1:
            for i in range(n):
                alice_candies += grid[i][0]
            break
        else:
            alice_candies += sum(grid[0])
            bob_candies += sum(grid[n-1])
            grid.pop(0)
            grid.pop(n-2)
            n -= 2
            for i in range(n):
                bob_candies += grid[i][0]
                grid[i].pop(0)
            for i in range(n):
                alice_candies += grid[i][m-2]
                grid[i].pop(m-2)
            m -= 2
    return max(alice_candies, bob_candies)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        grid = []
        for j in range(n):
            grid.append(list(map(int, input().split())))
        print(get_winner_candies(grid))