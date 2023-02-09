"""
"""

"""
t = int(input())
for i in range(t):
    n,m = list(map(int,input().split()))
    grid = []
    for j in range(n):
        row = list(map(int,input().split()))
        grid.append(row)
    alice_count = 0
    bob_count = 0
    while n != 0:
        min_count = min(grid[0])
        min_count_index = grid[0].index(min_count)
        alice_count += min_count
        grid.pop(min_count_index)
        n -= 1
    while m != 0:
        min_count = min(grid[0])
        min_count_index = grid[0].index(min_count)
        bob_count += min_count
        for i in range(n):
            grid[i].pop(min_count_index)
        m -= 1
    if alice_count > bob_count:
        print(alice_count)
    elif bob_count > alice_count:
        print(bob_count)
    else:
        print(alice_count + bob_count)
"""

t = int(input())
for i in range(t):
    n,m = list(map(int,input().split()))
    grid = []
    for j in range(n):
        row = list(map(int,input().split()))
        grid.append(row)
    alice_count = 0
    bob_count = 0
    while n != 0:
        min_count = min(grid[0])
        min_count_index = grid[0].index(min_count)
        alice_count += min_count
        grid.pop(min_count_index)
        n -= 1
    while m != 0:
        min_count = min(grid[0])
        min_count_index = grid[0].index(min_count)
        bob_count += min_count
        for i in range(n):
            grid[i].pop(min_count_index)
        m -= 1
    if alice_count > bob_count:
        print(alice_count)
    elif bob_count > alice_count:
        print(bob_count)
    else:
        print(alice_count + bob_count)