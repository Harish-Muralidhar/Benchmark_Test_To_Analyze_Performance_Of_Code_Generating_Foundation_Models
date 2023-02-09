'''
Example 3 : Cops in house 10 can cover houses 1 to 18, and cops in house 51 can cover houses 41 to 91. So, in total, 9 houses are safe.

'''

# Write your code here
def safe_houses(houses, cop_houses, speed, time):
    safe_houses = []
    for house in houses:
        flag = True
        for cop_house in cop_houses:
            if abs(house - cop_house) <= speed * time:
                flag = False
                break
        if flag:
            safe_houses.append(house)
    return len(safe_houses)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        m, x, y = map(int, input().split())
        cop_houses = list(map(int, input().split()))
        houses = [i for i in range(1, 101)]
        print(safe_houses(houses, cop_houses, x, y))