'''
Example 3 : Cops in house 10 can cover houses 1 to 18, and cops in house 51 can cover houses 41 to 91, leaving houses numbered 19 to 40, and 92 to 100 safe. So, in total 9 houses are safe.

'''

def safe_houses(houses, x, y):
    safe_houses = []
    for house in range(1, 101):
        if house not in houses:
            safe_houses.append(house)
        else:
            for cop in houses:
                if (abs(cop - house) <= x * y):
                    if house in safe_houses:
                        safe_houses.remove(house)
                    break
    return len(safe_houses)


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        M, x, y = map(int, input().split())
        houses = list(map(int, input().split()))
        print(safe_houses(houses, x, y))