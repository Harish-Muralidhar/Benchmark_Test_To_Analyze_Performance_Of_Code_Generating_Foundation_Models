'''

Explanation
Example case 1. There is no cell which is a centre of Prime-Cross.
Example case 2. The cells (2, 5), (4, 3), (4, 7) are centres of Prime-Cross.

'''
#Write your code here

import sys
import math

def isprime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def count_prime(L, R, T, B):
    ret = 0
    for x in range(min(L, R, T, B), 0, -1):
        if isprime(x):
            ret += 1
    return ret

def solve(r, c, matrix):
    ret = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] != "#":
                L = R = T = B = 0
                while j+R < c and matrix[i][j+R] == "^":
                    R += 1
                while j-L >= 0 and matrix[i][j-L] == "^":
                    L += 1
                while i+T < r and matrix[i+T][j] == "^":
                    T += 1
                while i-B >= 0 and matrix[i-B][j] == "^":
                    B += 1
                ret += count_prime(L, R, T, B)
    return ret

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        r, c = map(int, sys.stdin.readline().strip().split(" "))
        matrix = []
        for i in range(r):
            matrix.append(list(sys.stdin.readline().strip()))
        print solve(r, c, matrix)