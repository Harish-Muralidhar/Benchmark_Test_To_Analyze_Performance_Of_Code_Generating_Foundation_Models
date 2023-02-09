"""
"""

import sys

def get_max_area_intersection(rect1, rect2):
    """
    get max area of intersection of two rectangles
    """
    length = min(rect1[0], rect2[0])
    breadth = min(rect1[1], rect2[1])
    return length * breadth

def get_max_area_of_intersection(rectangles, num_rect_to_remove):
    """
    get max area of intersection of all rectangles,
    given we can remove at most num_rect_to_remove rectangles
    """
    rectangles.sort(key=lambda x: x[0] * x[1], reverse=True)
    max_area = 0
    for i in range(0, num_rect_to_remove + 1):
        # remove i rectangles from end
        remaining_rects = rectangles[:(-i)]
        # get max area of intersection of remaining rects
        max_area = max(max_area, get_max_area_of_intersection_remaining_rects(remaining_rects))
    return max_area

def get_max_area_of_intersection_remaining_rects(rectangles):
    """
    get max area of intersection of remaining rectangles,
    given they are sorted in decreasing order of area
    """
    if len(rectangles) == 1:
        return rectangles[0][0] * rectangles[0][1]
    max_area = 0
    for i in range(1, len(rectangles)):
        max_area = max(max_area, get_max_area_intersection(rectangles[i-1], rectangles[i]))
    return max_area

def get_inputs():
    """
    get inputs from stdin
    """
    num_test_cases = int(sys.stdin.readline())
    for _ in range(num_test_cases):
        num_rectangles, num_rectangles_to_remove = map(int, sys.stdin.readline().strip().split())
        rectangles = []
        for _ in range(num_rectangles):
            length, breadth = map(int, sys.stdin.readline().strip().split())
            rectangles.append([length, breadth])
        print(get_max_area_of_intersection(rectangles, num_rectangles_to_remove))

if __name__ == '__main__':
    get_inputs()