'''

'''

import math

def get_min_menus(p):
    if p == 1:
        return 1
    else:
        return math.floor(math.log(p, 2)) + 1

def main():
    T = int(input())
    for i in range(T):
        p = int(input())
        print(get_min_menus(p))

if __name__ == "__main__":
    main()