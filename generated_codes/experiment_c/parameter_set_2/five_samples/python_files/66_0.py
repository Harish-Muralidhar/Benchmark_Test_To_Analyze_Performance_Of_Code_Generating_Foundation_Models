'''

'''

import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = n // 10
        q = n - p
        g = gcd(p, q)
        print(p // g, q // g, sep='/')

if __name__ == '__main__':
    main()