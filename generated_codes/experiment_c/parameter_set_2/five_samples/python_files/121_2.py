'''


'''

import math

def get_distance(n):
    if n == 0:
        return 0
    if n == 1:
        return 2
    if n == 2:
        return 5
    if n == 3:
        return 8
    else:
        return 2*n + get_distance(n-2)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(get_distance(n))