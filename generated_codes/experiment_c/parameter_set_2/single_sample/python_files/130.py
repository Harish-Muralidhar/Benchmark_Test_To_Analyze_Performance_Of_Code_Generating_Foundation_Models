"""


"""

import math

def main():
    t = int(input())
    for i in range(t):
        p = input()
        print(solve(p))

def solve(p):
    days = 0
    jump = 1
    for i in range(1, len(p)):
        if p[i] == '#':
            jump = 1
        else:
            if jump == 1:
                days += 1
                jump += 1
    return days

if __name__ == '__main__':
    main()