"""

Explanation
There are two possible sequences of first two numbers: (1, 2) and (2, 1). If the first one is chosen then no shuffles are required. If the second one is chosen then after one shuffle we get (1, 2) and another shuffle is needed to sort the sequence. So the expected amount of shuffles is (1 * 0 + 1 * 2) / 2 = 1.

For sequence of length 6 the expected amount of shuffles is 1826/189.

For sequence of length 10 the expected amount of shuffles is 877318/35343.



"""



from fractions import Fraction

# def bogo_sort(arr):
#     """
#     :param: arr - array to sort
#     return type: list
#     return: array sorted in ascending order
#     """
#     # if the array is empty or has only one element, return that array since its already sorted
#     if len(arr) == 0 or len(arr) == 1:
#         return arr
#
#     while not is_sorted(arr):
#         # shuffle the array
#         shuffle(arr)
#     return arr
#
#
# def is_sorted(arr):
#     """
#     :param: arr - array
#     return type: boolean
#     return: true if elements in array are sorted in ascending order, else - False
#     """
#     # if the array is empty or has only one element, return true
#     if len(arr) == 0 or len(arr) == 1:
#         return True
#
#     for index in range(0, len(arr) - 1):
#         # compare current element with next element
#         if arr[index] > arr[index + 1]:
#             return False
#
#     # we didn't find any element violating the ascending order, so the array is sorted
#     return True
#
#
# def shuffle(arr):
#     """
#     :param: arr - array
#     return type: list
#     return: shuffled array
#     """
#     from random import randint
#     # if the array is empty or has only one element, return the array
#     if len(arr) <= 1:
#         return arr
#
#     last_index_in_the_array = len(arr) - 1
#
#     # walk through the array from beginning
#     for index_of_current_element in range(0, len(arr)):
#
#         # pick a random index from the array which is from the current index to the last index in the array
#         random_index = randint(index_of_current_element, last_index_in_the_array)
#
#         # if the random index is not the current index, swap them
#         if random_index != index_of_current_element:
#             arr[index_of_current_element], arr[random_index] = arr[random_index], arr[index_of_current_element]


def improved_bogo_sort(arr):
    """
    :param: arr - array to sort
    return type: list
    return: array sorted in ascending order
    """
    # if the array is empty or has only one element, return that array since its already sorted
    if len(arr) == 0 or len(arr) == 1:
        return arr

    # assign first index as 0 and last index as n-1
    first_index, last_index = 0, len(arr) - 1

    # index of the first element from left which is not fixed yet
    left = first_index
    # index of the first element from right which is not fixed yet
    right = last_index

    # keep looping until left and right cross each other
    while left <= right:
        # if left element is fixed, move left pointer
        if arr[left] == left + 1:
            left += 1
            continue

        # if right element is fixed, move right pointer
        if arr[right] == right + 1:
            right -= 1
            continue

        # if both left and right element are not fixed, fix the left and right element by swapping them
        arr[arr[left] - 1], arr[arr[right] - 1] = arr[arr[right] - 1], arr[arr[left] - 1]

    # after fixing all left and right elements,
    # walk through the array from left to right,
    # if the element is in its correct position, continue the loop
    # if not, shuffle the array and fix the leftmost element from left and rightmost element from right
    for i in range(len(arr)):
        if arr[i] == i + 1:
            continue

        # shuffle the array
        improved_shuffle(arr)

    return arr


def improved_shuffle(arr):
    """
    :param: arr - array
    return type: list
    return: shuffled array
    """
    from random import randint
    # if the array is empty or has only one element, return the array
    if len(arr) <= 1:
        return arr

    last_index_in_the_array = len(arr) - 1

    # walk through the array from beginning to the last but one index
    for index_of_current_element in range(0, last_index_in_the_array):

        # pick a random index from the array which is from the current index to the last index in the array
        random_index = randint(index_of_current_element, last_index_in_the_array)

        # if the random index is not the current index, swap them
        if random_index != index_of_current_element:
            arr[index_of_current_element], arr[random_index] = arr[random_index], arr[index_of_current_element]


def get_expected_number_of_shuffles_bogo_sort(n):
    """
    :param: n - size of array
    return type: float
    return: expected number of shuffles bogo sort takes to sort an array
    """
    # TODO: complete this method to get the answer for the problem
    # for the array of size n, the number of permutations possible is n!
    # for example, for array of size 3, the number of permutations possible is 3! = 6
    # these permutations can be visualised as follows:
    # [1,2,3]
    # [1,3,2]
    # [2,1,3]
    # [2,3,1]
    # [3,1,2]
    # [3,2,1]
    #
    # Now, we know that bogo sort takes some shuffles to sort the array
    # we need to calculate the expected number of shuffles
    # the expected number of shuffles will be the average of number of shuffles
    #
    # for example, for the first permutation, the array will be already sorted, so number of shuffles will be 0
    # for the second permutation, after 1 shuffle, the array will be sorted
    # for the third permutation, after 2 shuffles, the array will be sorted
    # for the fourth permutation, after 1 shuffle, the array will be sorted
    # for the fifth permutation, after 4 shuffles, the array will be sorted
    # for the sixth permutation, after 8 shuffles, the array will be sorted
    #
    # hence, the expected number of shuffles = (0+1+2+1+4+8)/6 = 16/6 = 2.66
    # similarly, you need to calculate the expected number of shuffles for array of size 'n'

    # factorial of n
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    # print(factorial)

    # initilize the list with the factorial number of permutations,
    # each permutation is a list
    permutations = []
    for i in range(1, n + 1):
        permutations.append([i])
    # print(permutations)

    # use the improved_bogo_sort function to get the number of shuffles
    # required to sort each permutation
    # and calculate the sum of all the shuffles, which is the numerator of the expected value
    numerator = 0
    for i in range(factorial - 1):
        improved_bogo_sort(permutations[i])
        numerator += permutations[i][0]
    # print(numerator)

    return numerator/factorial


def get_expected_number_of_shuffles_improved_bogo_sort(n):
    """
    :param: n - size of array
    return type: float
    return: expected number of shuffles bogo sort takes to sort an array
    """
    # TODO: complete this method to get the answer for the problem
    # for the array of size n, the number of permutations possible is n!
    # for example, for array of size 3, the number of permutations possible is 3! = 6
    # these permutations can be visualised as follows:
    # [1,2,3]
    # [1,3,2]
    # [2,1,3]
    # [2,3,1]
    # [3,1,2]
    # [3,2,1]
    #
    # Now, we know that bogo sort takes some shuffles to sort the array
    # we need to calculate the expected number of shuffles
    # the expected number of shuffles will be the average of number of shuffles
    #
    # for example, for the first permutation, the array will be already sorted, so number of shuffles will be 0
    # for the second permutation, after 1 shuffle, the array will be sorted
    # for the third permutation, after 2 shuffles, the array will be sorted
    # for the fourth permutation, after 1 shuffle, the array will be sorted
    # for the fifth permutation, after 4 shuffles, the array will be sorted
    # for the sixth permutation, after 8 shuffles, the array will be sorted
    #
    # hence, the expected number of shuffles = (0+1+2+1+4+8)/6 = 16/6 = 2.66
    # similarly, you need to calculate the expected number of shuffles for array of size 'n'

    # factorial of n
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    # print(factorial)

    # initilize the list with the factorial number of permutations,
    # each permutation is a list
    permutations = []
    for i in range(1, n + 1):
        permutations.append([i])
    # print(permutations)

    # use the improved_bogo_sort function to get the number of shuffles
    # required to sort each permutation
    # and calculate the sum of all the shuffles, which is the numerator of the expected value
    numerator = 0
    for i in range(factorial - 1):
        improved_bogo_sort(permutations[i])
        numerator += permutations[i][0]
    # print(numerator)

    return numerator/factorial


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    if is_sorted(arr):
        print("Pass")
    else:
        print("Fail")

    if solution == improved_bogo_sort(arr):
        print("Pass")
    else:
        print("Fail")


arr = [3, 5, 1, 6, 4, 2]
solution = [1, 2, 3, 4, 5, 6]

test_case = [arr, solution]
test_function(test_case)


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    if is_sorted(arr):
        print("Pass")
    else:
        print("Fail")

    if solution == improved_bogo_sort(arr):
        print("Pass")
    else:
        print("Fail")


arr = [3, 5, 1, 6, 4, 2]
solution = [1, 2, 3, 4, 5, 6]

test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5]
solution = [1, 2, 3, 4, 5]

test_case = [arr, solution]
test_function(test_case)

arr = [1]
solution = [1]

test_case = [arr, solution]
test_function(test_case)

arr = [2, 1]
solution = [1, 2]

test_case = [arr, solution]
test_function(test_case)

arr = [5, 4, 3, 2, 1]
solution = [1, 2, 3, 4, 5]

test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
solution = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

test_case = [arr, solution]
test_function(test_case)


def get_fraction(numerator, denominator):
    # TODO: complete this method to return the fraction in the form "numerator/denominator"
    # Type your code here

    return str(numerator) + "/" + str(denominator)


def get_fraction(numerator, denominator):
    # TODO: complete this method to return the fraction in the form "numerator/denominator"
    # Type your code here

    return str(numerator) + "/" + str(denominator)


def get_fraction(numerator, denominator):
    # TODO: complete this method to return the fraction in the form "numerator/denominator"
    # Type your code here

    return str(numerator) + "/" + str(denominator)


# print(get_fraction(5, 2))


for n in range(2, 151):
    print(Fraction(get_expected_number_of_shuffles_improved_bogo_sort(n)))