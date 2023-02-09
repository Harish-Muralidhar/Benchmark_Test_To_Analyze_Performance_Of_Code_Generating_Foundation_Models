"""
"""
import math
def game_over(nums):
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            return False
    return True

def play(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                nums[j] = abs(nums[j] - nums[i])
                break
        if game_over(nums):
            break
    return nums[0]


def input_output(func):
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = [int(x) for x in input().split()]
        ans = func(nums)
        print(ans)

input_output(play)