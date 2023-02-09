'''
For second query, 2 is directly connected to 3 by an edge. Hence distance 1.
For third query, 4 is connected to 3 by a path of length 3. Hence distance 3.

'''

def find_level(n):
    level = 0
    while n>0:
        n = n//2
        level += 1
    return level

def find_distance(i,j):
    if i==j:
        return 0
    level_i = find_level(i)
    level_j = find_level(j)
    if level_i == level_j:
        return abs(i-j)
    else:
        if level_i > level_j:
            return level_i - level_j + find_distance(i//2,j)
        else:
            return level_j - level_i + find_distance(i,j//2)

def main():
    n = int(input())
    for _ in range(n):
        i,j = map(int,input().split())
        print(find_distance(i,j))

main()