'''

'''

import math

def get_ways(n, m):
    return math.factorial(n*m)//(math.factorial(n)*math.factorial(m))

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()][0:2]
        print(get_ways(n, m))