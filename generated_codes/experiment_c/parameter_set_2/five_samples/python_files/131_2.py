"""

"""

# Write your code here
import math

def get_money(M, p):
    if p == 1:
        return 1000000000, 0
    if p == 0:
        return 0, 1000000000
    x = math.log(1000000000, p)
    if x > M:
        return 1000000000, 0
    else:
        return (1000000000 * p**x), (1000000000 * (1-p**x))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        M, p = map(float, input().split())
        print(' '.join(map(str, get_money(M, p))))