"""
"""
import random

"""
This is a solution for the problem.
"""


def solution(array):
    # generate a random array.
    a_array = [0] * len(array)
    for i in range(len(array)):
        j = random.randint(i, len(array)-1)
        for k in range(i, j+1):
            a_array[k] += 1
    # check whether a_array is acceptable, if not, generate another array.
    while not check_array(array, a_array):
        a_array = [0] * len(array)
        for i in range(len(array)):
            j = random.randint(i, len(array)-1)
            for k in range(i, j+1):
                a_array[k] += 1
    # return the acceptable array.
    return a_array


"""
This function is to check if an array is acceptable.
"""


def check_array(array, a_array):
    for i in range(len(array)):
        if array[i] < a_array[i]:
            return False
    return True

"""
This is a naive solution for the problem.
"""


def solution_naive(array):
    a_array = [0] * len(array)
    for i in range(len(array)):
        j = random.randint(i, len(array)-1)
        for k in range(i, j+1):
            a_array[k] += 1
        while not check_array(array, a_array):
            i = random.randint(0, len(array)-1)
            j = random.randint(i, len(array)-1)
            for k in range(i, j+1):
                a_array[k] += 1
    return a_array


"""
This is a faster solution for the problem.
"""


def solution_fast(array):
    a_array = [0] * len(array)
    for i in range(len(array)):
        j = random.randint(i, len(array)-1)
        a_array[i] += j-i+1
    while not check_array(array, a_array):
        a_array = [0] * len(array)
        for i in range(len(array)):
            j = random.randint(i, len(array)-1)
            a_array[i] += j-i+1
    return a_array


"""
Generate a random array for test
"""


def generate_array(n):
    array = []
    for i in range(n):
        array.append(random.randint(1, n))
    return array


"""
This is the main function.
"""


def main():
    array = generate_array(10)
    for i in range(4):
        print(solution_fast(array))


if __name__ == "__main__":
    main()