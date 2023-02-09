"""

Constraints

The values of X and Y will be at most 10,000 in absolute value.

"""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y)


def distance(p1, p2):
    return math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))


def get_distance(input_list, index):
    p1 = Point(input_list[index], input_list[index + 1])
    p2 = Point(input_list[index + 2], input_list[index + 3])
    return [p1, p2, distance(p1, p2)]


def get_coordinates(input_list):
    list1 = []
    for index in range(0, len(input_list), 2):
        value = get_distance(input_list, index)
        list1.append(Point(value[0].x, value[0].y))
    return list1


def is_triangle_possible(list1, r):
    if distance(list1[0], list1[1]) + distance(list1[2], list1[3]) <= r:
        return True
    return False


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        r = int(input())
        input_list = input().split(" ")
        input_list = list(map(int, input_list))
        list1 = get_coordinates(input_list)
        if is_triangle_possible(list1, r):
            print("yes")
        else:
            print("no")


if __name__ == '__main__':
    main()