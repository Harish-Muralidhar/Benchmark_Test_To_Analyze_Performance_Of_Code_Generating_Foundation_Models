'''


'''

import math

def solve(a, b):
    return int(math.log(b, 2)) - int(math.log(a, 2))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(solve(a, b))