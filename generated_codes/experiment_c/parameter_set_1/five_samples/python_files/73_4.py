"""

Explanation
In the first example, the first four frequencies in the given sequence are in arithmetic progression and the last four frequencies in the given sequence are in geometric progression.
In the second example, the frequencies at indices 2 and 4 are swapped.
"""

# Write your code here
# import the library
import numpy as np

# function to find the first and last index which satisfy the Arithmetic progression
def find_index(arr, v1, v2, v3):
    # store the values of differnce of the frequency
    val1 = v2-v1
    val2 = v3-v2
    # if values are same return -1
    if val1==val2:
        return -1
    # if first value is greater than second value then find the last index
    if val1>val2:
        l = len(arr)
        temp = v3
        while temp<=arr[l-1]:
            if temp in arr:
                i = arr.index(temp)
            temp+=val2
        return i
    # else find the first index
    else:
        temp = v3
        while temp>=arr[0]:
            if temp in arr:
                i = arr.index(temp)
            temp-=val1
        return i

# function to find the common ratio of the sequence
def common_ratio(arr, v1, v2, v3):
    # store the values of differnce of the frequency
    val1 = v2-v1
    val2 = v3-v2
    # if values are same return -1
    if val1==val2:
        return -1
    # if first value is greater than second value then find the last index
    if val1>val2:
        return val2
    # else find the first index
    else:
        return val1

# function to find the first and last index which satisfy the Geometric progression
def find_index_G(arr, v1, v2, v3):
    # store the values of differnce of the frequency
    val1 = v2/v1
    val2 = v3/v2
    # if values are same return -1
    if val1==val2:
        return -1
    # if first value is greater than second value then find the last index
    if val1>val2:
        l = len(arr)
        temp = v3
        while temp<=arr[l-1]:
            if temp in arr:
                i = arr.index(temp)
            temp = temp*val2
        return i
    # else find the first index
    else:
        temp = v3
        while temp>=arr[0]:
            if temp in arr:
                i = arr.index(temp)
            temp = temp/val1
        return i

# function to find the common ratio of the sequence
def common_ratio_G(arr, v1, v2, v3):
    # store the values of differnce of the frequency
    val1 = v2/v1
    val2 = v3/v2
    # if values are same return -1
    if val1==val2:
        return -1
    # if first value is greater than second value then find the last index
    if val1>val2:
        return val2
    # else find the first index
    else:
        return val1

# function to find the arithmetic progression
def find_arithmetic(arr, v1, v2, v3):
    # store the values of differnce of the frequency
    val1 = v2-v1
    val2 = v3-v2
    # if values are same return -1
    if val1==val2:
        return -1
    # if first value is greater than second value then find the last index
    if val1>val2:
        l = len(arr)
        temp = v3
        temp_arr = []
        while temp<=arr[l-1]:
            if temp in arr:
                temp_arr.append(temp)
            temp+=val2
        return temp_arr
    # else find the first index
    else:
        temp = v3
        temp_arr = []
        while temp>=arr[0]:
            if temp in arr:
                temp_arr.append(temp)
            temp-=val1
        return temp_arr

# function to find the geometric progression
def find_geometric(arr, v1, v2, v3):
    # store the values of differnce of the frequency
    val1 = v2/v1
    val2 = v3/v2
    # if values are same return -1
    if val1==val2:
        return -1
    # if first value is greater than second value then find the last index
    if val1>val2:
        l = len(arr)
        temp = v3
        temp_arr = []
        while temp<=arr[l-1]:
            if temp in arr:
                temp_arr.append(temp)
            temp = temp*val2
        return temp_arr
    # else find the first index
    else:
        temp = v3
        temp_arr = []
        while temp>=arr[0]:
            if temp in arr:
                temp_arr.append(temp)
            temp = temp/val1
        return temp_arr

# main function
if __name__ == '__main__':
    # take the number of test cases
    t = int(input())
    # loop through all the test cases
    while t>0:
        # take the size of the array
        n = int(input())
        # take the input array
        arr = list(map(int, input().strip().split()))
        # find the index in which the array contains the arithmetic progression
        i = find_index(arr, arr[0], arr[1], arr[2])
        # check if the index is not -1
        if i!=-1:
            # find the arithmetic progression
            a = find_arithmetic(arr, arr[0], arr[1], arr[2])
            # find the geometric progression
            g = find_geometric(arr, arr[i-1], arr[i], arr[i+1])
        # if index is -1 then find the index in which the array contains the geometric progression
        else:
            i = find_index_G(arr, arr[0], arr[1], arr[2])
            # find the arithmetic progression
            g = find_geometric(arr, arr[0], arr[1], arr[2])
            # find the geometric progression
            a = find_arithmetic(arr, arr[i-1], arr[i], arr[i+1])
        # convert the array into numpy array
        a = np.array(a)
        g = np.array(g)
        # print the arrays
        print(*a)
        print(*g)
        # decrement the number of test case
        t-=1