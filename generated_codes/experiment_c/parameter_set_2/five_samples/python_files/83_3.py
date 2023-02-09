"""

"""

import sys

def min_segment_sum(N, K, P, nums):
    """
    Find the minimum segment sum modulo P that is at least K.
    """
    # TODO: Implement me
    return 0

if __name__ == '__main__':
    # Read the input
    N, K, P = [int(i) for i in sys.stdin.readline().split()]
    nums = [int(i) for i in sys.stdin.readlines()]

    # Compute the answer
    answer = min_segment_sum(N, K, P, nums)

    # Output the answer
    print(answer)