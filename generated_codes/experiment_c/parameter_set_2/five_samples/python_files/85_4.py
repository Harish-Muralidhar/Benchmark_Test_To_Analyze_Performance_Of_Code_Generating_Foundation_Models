'''

'''

# Solution

import math

def countPairs(n, u, v):
    if u == v:
        return n
    if u > v:
        u, v = v, u
    if u == 1:
        return 1
    if v % 2 == 0:
        if u == v // 2:
            return 1
        else:
            return 2
    else:
        if u == (v - 1) // 2:
            return 1
        else:
            return 2

def solve(n, u, v):
    if u == v:
        return n
    if u > v:
        u, v = v, u
    if u == 1:
        return 1
    if v % 2 == 0:
        if u == v // 2:
            return 1
        else:
            return 2
    else:
        if u == (v - 1) // 2:
            return 1
        else:
            return 2

def solve2(n, u, v):
    if u == v:
        return n
    if u > v:
        u, v = v, u
    if u == 1:
        return 1
    if v % 2 == 0:
        if u == v // 2:
            return 1
        else:
            return 2
    else:
        if u == (v - 1) // 2:
            return 1
        else:
            return 2

def solve3(n, u, v):
    if u == v:
        return n
    if u > v:
        u, v = v, u
    if u == 1:
        return 1
    if v % 2 == 0:
        if u == v // 2:
            return 1
        else:
            return 2
    else:
        if u == (v - 1) // 2:
            return 1
        else:
            return 2

def solve4(n, u, v):
    if u == v:
        return n
    if u > v:
        u, v = v, u
    if u == 1:
        return 1
   