'''

'''

def bico_grid(r,c,g):
    moves = []
    while g > 0:
        if r >= c:
            moves.append(c)
            g -= c
            r -= 1
        else:
            moves.append(r)
            g -= r
            c -= 1
    return len(moves), moves

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        r,c,g = map(int, input().split())
        k, moves = bico_grid(r,c,g)
        print(k)
        print(*moves)