'''
Example 3 : Cops in house 10 can cover houses 1 to 10 and cops in house 51 can cover houses 41 to 51. So, in total, there are 9 safe houses.
'''


def safe_houses(chip_houses, position, max_speed, max_time):
    safe_house_count = 0
    for house in range(1, 101):
        for chip in chip_houses:
            speed = abs(house - chip) / max_time
            if speed <= max_speed:
                break
        else:
            safe_house_count += 1
    return safe_house_count


if __name__ == '__main__':
    test_count = int(input())
    for test in range(test_count):
        chip_count, max_speed, max_time = map(int, input().split())
        chip_houses = list(map(int, input().split()))
        safe_houses_count = safe_houses(chip_houses, position, max_speed, max_time)
        print(safe_houses_count)