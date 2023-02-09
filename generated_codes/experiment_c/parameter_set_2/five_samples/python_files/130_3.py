"""


"""

import sys

def main():
    t = int(sys.stdin.readline())
    while t:
        t -= 1
        s = sys.stdin.readline()
        s = s.strip()
        i = 0
        j = 0
        ans = 0
        while i < len(s):
            if s[i] == '.':
                j = i
                while j < len(s) and s[j] == '.':
                    j += 1
                ans += 1
                i = j
            else:
                i += 1
        print ans

if __name__ == '__main__':
    main()