'''

'''

import sys

def main():
    n = int(input())
    for i in range(n):
        s1 = input()
        s2 = input()
        min_diff = 0
        max_diff = 0
        diff = 0
        for j in range(len(s1)):
            if s1[j] == '?' or s2[j] == '?':
                max_diff += 1
            else:
                if s1[j] != s2[j]:
                    diff += 1
        min_diff = diff
        print(min_diff, max_diff)

if __name__ == "__main__":
    main()