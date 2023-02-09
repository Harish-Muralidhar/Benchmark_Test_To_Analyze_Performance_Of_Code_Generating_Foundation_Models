"""


"""

import sys

def main():
    testcases = int(sys.stdin.readline())
    for i in range(testcases):
        n = int(sys.stdin.readline())
        s = [int(x) for x in sys.stdin.readline().split()]
        t = [int(x) for x in sys.stdin.readline().split()]
        print(get_min_max_diff(s, t))

def get_min_max_diff(s, t):
    s_diff = [0] * len(s)
    t_diff = [0] * len(t)
    for i in range(len(s)):
        if i == 0:
            s_diff[0] = s[0]
            t_diff[0] = t[0]
        else:
            s_diff[i] = s[i] - s[i-1]
            t_diff[i] = t[i] - t[i-1]
    s_diff.sort()
    t_diff.sort()
    s_max = s_diff[-1]
    t_max = t_diff[-1]
    s_max_index = s_diff.index(s_max)
    t_max_index = t_diff.index(t_max)
    if s_max_index == 0:
        s_max_index = 1
    if t_max_index == 0:
        t_max_index = 1
    if s_max_index < t_max_index:
        return "A" * s_max_index + "B" * t_max_index
    else:
        return "A" * t_max_index + "B" * s_max_index

if __name__ == '__main__':
    main()