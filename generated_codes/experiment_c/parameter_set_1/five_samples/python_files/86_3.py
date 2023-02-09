"""


"""

def get_neigbours(point, n, m, pool):
    x, y = point
    neighbours = []
    if x < n and y < m and pool[x][y] > 0:
        if x + 1 < n:
            neighbours.append((x+1, y))
        if x + 2 < n:
            neighbours.append((x+2, y))
        if x - 1 >= 0:
            neighbours.append((x-1, y))
        if x - 2 >= 0:
            neighbours.append((x-2, y))
        if y + 1 < m:
            neighbours.append((x, y+1))
        if y + 2 < m:
            neighbours.append((x, y+2))
        if y - 1 >= 0:
            neighbours.append((x, y-1))
        if y - 2 >= 0:
            neighbours.append((x, y-2))
    return neighbours

def dfs(pool, start_point, end_point, n, m):
    stack = [start_point]
    path = []
    # remove cell from pool
    pool[start_point[0]][start_point[1]] -= 1
    while stack:
        v = stack.pop()
        path.append(v)
        if v == end_point:
            return path
        neighbours = get_neigbours(v, n, m, pool)
        for u in neighbours:
            # remove cell from pool
            pool[u[0]][u[1]] -= 1
            stack.append(u)
    return None

def main():
    t = int(input())

    for i in range(t):
        n, m = map(int, input().split())
        sx, sy = map(int, input().split())
        fx, fy = map(int, input().split())
        pool = []
        for i in range(n):
            pool.append(list(map(int, input().split())))

        # initial state of the pool
        #print(pool)
        stack = [(sx-1, sy-1)]
        paths = []
        while stack:
            v = stack.pop()
            path = dfs(pool, v, (fx-1, fy-1), n, m)
            #print(path)
            if path is not None:
                paths.append(path)
                # reset pool
                for i in range(n):
                    for j in range(m):
                        pool[i][j] = pool[i][j] + 1
            neighbours = get_neigbours(v, n, m, pool)
            for u in neighbours:
                # remove cell from pool
                pool[u[0]][u[1]] -= 1
                stack.append(u)
        # print number of paths
        print(len(paths))

if __name__ == '__main__':
    main()