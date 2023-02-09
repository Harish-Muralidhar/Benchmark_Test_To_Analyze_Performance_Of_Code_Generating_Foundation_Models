"""


"""

import sys
from collections import deque

def main():
    # read the input
    N, M, Q = map(int, sys.stdin.readline().strip().split())
    Sx, Sy = map(int, sys.stdin.readline().strip().split())
    P1 = [0]*6
    P2 = [0]*6
    for i in range(6):
        P1[i], P2[i] = map(int, sys.stdin.readline().strip().split())
    T = []
    for i in range(Q):
        T.append(int(sys.stdin.readline().strip()))
    
    # calculate the result
    result = []
    for t in T:
        result.append(calculate(N, M, Q, Sx, Sy, P1, P2, t))
    
    # output the result
    for r in result:
        print(r)

def calculate(N, M, Q, Sx, Sy, P1, P2, t):
    # create the grid
    grid = [[0]*M for i in range(N)]
    grid[Sx-1][Sy-1] = 1
    
    # create the queue
    queue = deque()
    queue.append((Sx-1, Sy-1))
    
    # create the direction
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    
    # create the direction map
    direction_map = {0: [0, 1], 1: [1, 2], 2: [0, 2], 3: [2, 1], 4: [1, 0], 5: [2, 0]}
    
    # do the move
    for i in range(t):
        # create the new queue
        new_queue = deque()
        
        # create the new grid
        new_grid = [[0]*M for i in range(N)]
        
        # do the move
        while len(queue) > 0:
            # get the current position