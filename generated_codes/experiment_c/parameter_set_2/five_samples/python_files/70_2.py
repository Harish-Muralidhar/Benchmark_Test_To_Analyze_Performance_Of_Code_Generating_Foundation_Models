"""

"""

import math

def subset_sum(nums):
    """
    :param nums: list of numbers
    :return: list of numbers
    """
    nums.sort()
    n = len(nums)
    max_sum = nums[-1]
    max_sum_bin = bin(max_sum)[2:]
    max_sum_bin_len = len(max_sum_bin)
    res = [0] * max_sum_bin_len
    for i in range(n):
        nums[i] = bin(nums[i])[2:]
    for i in range(n):
        for j in range(max_sum_bin_len):
            if j < len(nums[i]):
                res[j] += int(nums[i][j])
    for i in range(max_sum_bin_len):
        res[i] = res[i] % 2
    res = [str(i) for i in res]
    res = int("".join(res), 2)
    return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:]
        print(subset_sum(arr))