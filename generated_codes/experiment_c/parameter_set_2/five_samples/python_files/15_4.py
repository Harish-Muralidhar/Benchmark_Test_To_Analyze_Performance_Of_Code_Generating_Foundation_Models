'''
Example 3 : Cops in house 10 can cover houses 1 to 19, and cops in house 51 can cover houses 35 to 65, leaving houses numbered 20 to 34, and 66 to 100 safe. So, in total 35-20+100-66 = 9 houses are safe.
'''

import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        M, x, y = map(int, sys.stdin.readline().split())
        cop_houses = set(map(int, sys.stdin.readline().split()))
        houses_covered = set()
        for house in cop_houses:
            houses_covered.update(range(house-x*y, house+x*y+1))
        print(100 - len(houses_covered))

if __name__ == '__main__':
    main()