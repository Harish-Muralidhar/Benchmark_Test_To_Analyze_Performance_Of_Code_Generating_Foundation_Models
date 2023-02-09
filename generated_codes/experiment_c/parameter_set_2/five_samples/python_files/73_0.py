"""

Note
The first sample input has been handcrafted to make the problem more understandable.

Explanation
Example case 1: Joe will play the beats (2, 5, 8, 11) while Chef will play the beats (4, 8, 16).
Example case 2: Joe will play the beats (2, 3, 4, 5) while Chef will play the beats (2, 4, 8).
Example case 3: Joe will play the beats (2, 3, 9, 10, 19, 27, 28) while Chef will play the beats (8, 16).
Example case 4: Joe will play the beats (4, 7, 10, 13, 25) while Chef will play the beats (2, 4, 8, 16).

"""

# cook your dish here

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def is_power_of_two(n):
    if n == 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True

def find_common_ratio(arr):
    if len(arr) == 2:
        return arr[1] // arr[0]
    common_ratio = arr[1] // arr[0]
    for i in range(2, len(arr)):
        common_ratio = gcd(common_ratio, arr[i] // arr[i - 1])
    return common_ratio

def find_arithmetic_progression(arr, common_diff):
    new_arr = []
    for i in range(len(arr) - 1):
        new_arr.append(arr[i] + common_diff)
    return new_arr

def find_geometric_progression(arr, common_ratio):
    new_arr = []
    for i in range(len(arr) - 1):
        new_arr.append(arr[i] * common_ratio)
