"""


"""

import math

def equal_pieces(n):
    if n == 1:
        return True
    if n == 2:
        return False
    return True

def possible_pieces(n):
    if n == 1:
        return True
    if n == 2:
        return False
    return True

def possible_pieces_not_equal(n):
    if n == 1:
        return True
    if n == 2:
        return False
    return True

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(equal_pieces(n), possible_pieces(n), possible_pieces_not_equal(n))

if __name__ == '__main__':
    main()