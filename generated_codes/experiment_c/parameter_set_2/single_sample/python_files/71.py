'''

'''

# import the necessary libraries
import random

# define the function to solve the problem
def solution(n, b):
    # initialize the array A with zeros
    a = [0] * n
    # loop through the array B
    for i in range(n):
        # generate a random index j such that j is greater or equal to i
        j = random.randint(i, n - 1)
        # increment A[i], A[i+1], A[i+2] ... A[j] by 1
        for k in range(i, j + 1):
            a[k] += 1
    # check if for any index i, A[i] is greater than B[i]
    for i in range(n):
        if a[i] > b[i]:
            return 0
    return 1

# get the number of test cases
test_cases = int(input())
# loop through the test cases
for i in range(test_cases):
    # get the number of elements
    n = int(input())
    # get the array B
    b = list(map(int, input().split()))
    # get the number of different arrays A
    print(solution(n, b))