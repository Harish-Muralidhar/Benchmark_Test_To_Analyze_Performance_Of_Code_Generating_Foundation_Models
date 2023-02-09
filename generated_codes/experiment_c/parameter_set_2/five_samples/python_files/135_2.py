'''
For second query, 2 is directly connected to 3 by an edge. Hence distance 1.
For third query, 4 is connected to 3 via node 2. Hence distance 2.

'''

import math

def get_distance(node1, node2):
    if node1 == node2:
        return 0
    if node1 > node2:
        node1, node2 = node2, node1
    while node1 != node2:
        if node1 % 2 == 0:
            node1 = node1 // 2
        else:
            node1 = (node1 - 1) // 2
        if node2 % 2 == 0:
            node2 = node2 // 2
        else:
            node2 = (node2 - 1) // 2
    return int(math.log(node1, 2))

def main():
    n = int(input())
    for i in range(n):
        node1, node2 = map(int, input().split())
        print(get_distance(node1, node2))

if __name__ == '__main__':
    main()