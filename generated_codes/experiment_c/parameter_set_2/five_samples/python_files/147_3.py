"""

"""

import sys

def main():
    test_cases = int(sys.stdin.readline())
    for i in range(test_cases):
        n = int(sys.stdin.readline())
        speed = list(map(int, sys.stdin.readline().split()))
        max_speed = speed[0]
        count = 1
        for s in speed[1:]:
            if s <= max_speed:
                max_speed = s
            else:
                count += 1
        print(count)

if __name__ == '__main__':
    main()