"""

"""

def max_area(rectangles, m):
    """
    :param rectangles: list of rectangles
    :param m: number of rectangles to remove
    :return: maximum area of intersection
    """
    # TODO: Write your code here
    return 0


def test_function(test_case):
    rectangles = test_case[0]
    m = test_case[1]
    solution = test_case[2]
    output = max_area(rectangles, m)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


rectangles = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
m = 2
solution = 20
test_case = [rectangles, m, solution]
test_function(test_case)

rectangles = [[2, 1], [2, 3], [3, 4], [4, 5], [5, 6]]
m = 2
solution = 24
test_case = [rectangles, m, solution]
test_function(test_case)

rectangles = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
m = 3
solution = 0
test_case = [rectangles, m, solution]
test_function(test_case)

rectangles = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
m = 5
solution = 1
test_case = [rectangles, m, solution]
test_function(test_case)

rectangles = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
m = 3
solution = 0
test_case = [rectangles, m, solution]
test_function(test_case)