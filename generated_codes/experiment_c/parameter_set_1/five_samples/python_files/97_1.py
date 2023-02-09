"""

Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.

Code:

import sys

def main():

# Read the input
    T = int(raw_input())
    for i in range(T):
        m, n = map(int, raw_input().split(' '))
        grid = []
        iter_n = 0
        while iter_n < n:
            grid.append(map(int, raw_input().split(' ')))
            iter_n += 1
        print (find_winner(grid, m, n))

def find_winner(grid, m, n):
    bob_count = 0
    alice_count = 0
    while m > 0 and n > 0:
        find = False
        minimum = sys.maxint
        row = 0
        col = 0
        iter_n = 0
        iter_m = 0
        for row in grid:
            for col in row:
                if col < minimum:
                    minimum = col
                    row_number = iter_m
                    col_number = iter_n
                    find = True
                iter_n += 1
            iter_n = 0
            iter_m += 1
        if m > 1 and n > 1:
            if find:
                if row_number == 0:
                    alice_count += minimum
                    grid.remove(grid[row_number])
                    n -= 1
                elif row_number == m - 1:
                    alice_count += minimum
                    grid.remove(grid[row_number])
                    n -= 1
                elif col_number == 0:
                    alice_count += minimum
                    for i in range(m):
                        grid[i].remove(grid[i][col_number])
                    m -= 1
                else:
                    alice_count += minimum
                    for i in range(m):
                        grid[i].remove(grid[i][col_number])
                    m -= 1
            else:
                if row_number == 0:
                    bob_count += minimum
                    grid.remove(grid[row_number])
                    n -= 1
                elif row_number == m - 1:
                    bob_count += minimum
                    grid.remove(grid[row_number])
                    n -= 1
                elif col_number == 0:
                    bob_count += minimum
                    for i in range(m):
                        grid[i].remove(grid[i][col_number])
                    m -= 1
                else:
                    bob_count += minimum
                    for i in range(m):
                        grid[i].remove(grid[i][col_number])
                    m -= 1
        else:
            if m == 1:
                for i in range(m):
                    bob_count += grid[i][col_number]
                break
            elif n == 1:
                for i in range(n):
                    bob_count += grid[row_number][i]
                break
    if bob_count > alice_count:
        return bob_count
    elif alice_count > bob_count:
        return alice_count
    else:
        return bob_count + alice_count

main()

"""

# solution 2:

from collections import deque

def main():
    test = int(input())
    for i in range(test):
        m,n = map(int, input().split())
        grid = []
        for j in range(m):
            grid.append(list(map(int, input().split())))
        print(find_winner(grid, m, n))
        
def find_winner(grid, m, n):
    alice_count = 0
    bob_count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == min(grid[i]):
                alice_count += grid[i][j]
                grid[i][j] = float('inf')
            if grid[i][j] == min([grid[x][j] for x in range(m)]):
                alice_count += grid[i][j]
                grid[i][j] = float('inf')
    for i in range(m):
        for j in range(n):
            bob_count += grid[i][j]
    if alice_count > bob_count:
        return alice_count
    elif alice_count < bob_count:
        return bob_count
    else:
        return alice_count + bob_count

main()