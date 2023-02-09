"""

"""

import sys

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        speeds = [int(x) for x in input().split()]
        max_speed = max(speeds)
        print(speeds.count(max_speed))

main()