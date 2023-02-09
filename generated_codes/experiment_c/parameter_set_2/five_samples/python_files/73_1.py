'''

Explanation
Example case 1: Joe will play the beats (2, 5, 8, 11) while Chef will play the beats (4, 8, 16).
Example case 2: Joe will play the beats (2, 3, 4, 5) while Chef will play the beats (1, 2, 4).
Example case 3: Joe will play the beats (2, 3, 9, 10, 19, 27, 28) while Chef will play the beats (1, 3, 9, 27, 81).
Example case 4: Joe will play the beats (4, 7, 10, 13, 25) while Chef will play the beats (1, 4, 10, 25).

'''

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def get_arithmetic_progression(nums):
    if len(nums) == 2:
        return nums
    diff = nums[1] - nums[0]
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] != diff:
            return nums[:i]
    return nums

def get_geometric_progression(nums):
    if len(nums) == 2:
        return nums
    ratio = nums[1] / nums[0]
    for i in range(1, len(nums)):
        if nums[i] / nums[i - 1] != ratio:
            return nums[:i]
    return nums

def get_arithmetic_progression_from_geometric(nums):
    if len(nums) == 2:
        return nums
    ratio = nums[1] / nums[0]
    for i in range(1, len(nums)):
        if nums[i] / nums[i - 1] != ratio:
            return nums[:i]
    return nums

def get_geometric_