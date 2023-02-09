"""

"""

import sys

def main():
    test_case = int(sys.stdin.readline())
    for i in range(test_case):
        n = int(sys.stdin.readline())
        speed_list = list(map(int, sys.stdin.readline().split()))
        max_speed = speed_list[0]
        count = 0
        for j in range(n):
            if speed_list[j] <= max_speed:
                count += 1
                max_speed = speed_list[j]
        print(count)

if __name__ == '__main__':
    main()