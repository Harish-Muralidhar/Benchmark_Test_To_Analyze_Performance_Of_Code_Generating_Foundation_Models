'''
Example 3 : Cops in house 10 can cover houses 1 to 18, and cops in house 51 can cover houses 41 to 91. So, in total, 18 houses are not safe.

'''

def safe_houses(houses, cops, x, y):
    safe_houses = []
    for house in houses:
        safe = True
        for cop in cops:
            if abs(house - cop) <= (x * y):
                safe = False
                break
        if safe:
            safe_houses.append(house)
    return safe_houses

def main():
    T = int(input())
    for _ in range(T):
        M, x, y = map(int, input().split())
        cops = list(map(int, input().split()))
        houses = list(range(1, 101))
        safe_houses = safe_houses(houses, cops, x, y)
        print(len(safe_houses))

if __name__ == '__main__':
    main()