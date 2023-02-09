'''
For second query, 2 is connected to 3 by an edge. Hence distance 1.
For third query, 4 is connected to 3 by a path of length 3. Hence distance 3.

'''

import math

def get_distance(i, j):
    if i == j:
        return 0
    else:
        i_level = int(math.log2(i))
        j_level = int(math.log2(j))
        if i_level == j_level:
            return abs(i - j)
        else:
            return get_distance(i, 2**i_level) + get_distance(2**j_level, j)

def main():
    n = int(input())
    for i in range(n):
        i, j = map(int, input().split())
        print(get_distance(i, j))

if __name__ == '__main__':
    main()