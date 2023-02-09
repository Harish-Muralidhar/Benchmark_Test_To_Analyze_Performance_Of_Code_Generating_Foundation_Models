'''

Example 3


Input:
7 5
....@
.....
......
D...D
......
.....
$....

Output:
4



Example 4


Input:
7 5
....@
.....
......
D.....
......
.....
$....

Output:
3

'''

from collections import deque
def read_file():
    '''
    read the input file and return a 2d list
    '''
    with open('input_spoon.txt', 'r') as f:
        row, col = map(int, f.readline().split())
        graph = [list(f.readline().strip()) for _ in range(row)]
        return graph

def find_chef(graph):
    '''
    find the location of the chef
    '''
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == '@':
                chef = (i,j)
                return chef

def find_spoon(graph):
    '''
    find the location of the spoon
    '''
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == '$':
                spoon = (i,j)
                return spoon

def find_monsters(graph):
    '''
    find the location of all the monsters
    '''
    monsters = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 'D':
                monsters.append((i,j))
    return monsters

def bfs(graph, start, end):
    '''
    BFS implementation
    '''
    row, col = len(graph), len(graph[0])
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        node, dist = queue.popleft()
        if node not in visited:
            visited.add(node)
            neighbors = [(node[0] + 1, node[1]), (node[0] - 1, node[1]), (node[0], node[1] + 1), (node[0], node[1] - 1)]
            for neighbor in neighbors:
                if neighbor[0] < 0 or neighbor[0] >= row or neighbor[1] < 0 or neighbor[1] >= col:
                    continue
                if graph[neighbor[0]][neighbor[1]] == 'D':
                    return dist + 1
                elif graph[neighbor[0]][neighbor[1]] != '.':
                    continue
                queue.append((neighbor, dist + 1))
    return -1

def main():
    graph = read_file()
    chef = find_chef(graph)
    spoon = find_spoon(graph)
    monsters = find_monsters(graph)
    distances = [bfs(graph, chef, monster) for monster in monsters]
    print(distances)
    dist = min(distances)
    print(dist)

if __name__ == '__main__':
    main()