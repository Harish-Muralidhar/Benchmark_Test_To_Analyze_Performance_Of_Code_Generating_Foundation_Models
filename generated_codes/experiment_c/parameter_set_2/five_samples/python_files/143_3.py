"""

"""

import sys

def main():
    test_cases = int(sys.stdin.readline().strip())

    for i in range(test_cases):
        k = int(sys.stdin.readline().strip())
        s = sys.stdin.readline().strip()
        if len(s) == 1:
            print(s)
            continue
        if len(s) == 2:
            if s[0] == s[1]:
                print("NO")
                continue
            else:
                print(s)
                continue
        if len(s) > 2:
            if s[0] == s[1]:
                if s[1] == s[2]:
                    print("NO")
                    continue
                else:
                    s = s[1:] + s[0]
                    print(s)
                    continue
            else:
                if s[0] == s[-1]:
                    print("NO")
                    continue
                else:
                    print(s)
                    continue

if __name__ == "__main__":
    main()