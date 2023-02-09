'''

'''

import math

def get_min_menus(p):
    menu_price = [2**i-1 for i in range(1,13)]
    menu_price.sort(reverse=True)
    menu_count = 0
    while p > 0:
        for price in menu_price:
            if p >= price:
                p -= price
                menu_count += 1
                break
    return menu_count

def main():
    t = int(input())
    for i in range(t):
        p = int(input())
        print(get_min_menus(p))

if __name__ == "__main__":
    main()