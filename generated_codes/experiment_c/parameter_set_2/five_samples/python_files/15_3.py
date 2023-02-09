"""
Example 3 : Cops in house 10 can cover houses 1 to 18, and cops in house 51 can cover houses 41 to 91, leaving houses numbered 19 to 40, and 92 to 100 safe. So, in total 9 houses are safe.

"""

def safe_houses(houses, speed, time, cops):
    safe_houses = []
    for house in houses:
        if house not in cops:
            safe_houses.append(house)
    return safe_houses

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        M, x, y = map(int, input().split())
        cops = list(map(int, input().split()))
        houses = [i for i in range(1, 101)]
        print(len(safe_houses(houses, x, y, cops)))