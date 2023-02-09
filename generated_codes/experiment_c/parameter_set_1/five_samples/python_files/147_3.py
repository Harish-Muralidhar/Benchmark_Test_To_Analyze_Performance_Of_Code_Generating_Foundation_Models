"""
"""

for i in range(int(input())):

    N = int(input())
    speed = [int(x) for x in input().split()]

    """
    # Brute Force
    # Time Limit Exceeded
    count = 0
    for i in range(N-1):
        if speed[i] <= speed[i+1]:
            count += 1
    print(count)
    """

    # Sorting
    # Time Limit Exceeded
    speed.sort()
    print(len(speed)-1)