"""

"""

import math

def get_money(M, p):
    if M == 0:
        return 0
    else:
        return math.pow(p, M)

def get_money_divide(M, p):
    if M == 0:
        return 0
    else:
        return math.pow(p, M) / 2

def main():
    T = int(input())
    for i in range(T):
        M, p = map(float, input().split())
        print(get_money_divide(M, p), get_money_divide(M, p))

if __name__ == "__main__":
    main()