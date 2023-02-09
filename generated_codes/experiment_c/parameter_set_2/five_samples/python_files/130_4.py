"""


"""

import sys

def main():
    testcases = int(sys.stdin.readline().strip())
    for i in range(testcases):
        line = sys.stdin.readline().strip()
        print(solve(line))

def solve(line):
    max_jump = 1
    jumps = 0
    for i in range(1, len(line)):
        if line[i] == '.':
            continue
        if i > max_jump:
            jumps += 1
            max_jump = i + max_jump
    return jumps

if __name__ == '__main__':
    main()