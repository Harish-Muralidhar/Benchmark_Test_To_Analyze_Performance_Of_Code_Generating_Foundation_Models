"""


"""

import math

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return (a*b) // gcd(a, b)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        print(gcd(a, b), lcm(a, b))