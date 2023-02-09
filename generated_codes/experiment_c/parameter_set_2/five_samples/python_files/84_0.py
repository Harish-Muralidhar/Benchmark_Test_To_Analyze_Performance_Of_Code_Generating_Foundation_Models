'''

'''

import math

def binomial(n, k):
    if k > n - k:
        k = n - k
    b = 1
    for i in range(k):
        b = b * (n - i)
        b = b // (i + 1)
    return b

def find_coins(r, c, g):
    coins = []
    while g > 0:
        if c == 0:
            break
        if binomial(r, c) <= g:
            coins.append(binomial(r, c))
            g -= binomial(r, c)
            r -= 1
            c -= 1
        else:
            r -= 1
    return coins

def main():
    t = int(input())
    for _ in range(t):
        r, c, g = map(int, input().split())
        coins = find_coins(r, c, g)
        print(len(coins))
        print(*coins)

if __name__ == "__main__":
    main()