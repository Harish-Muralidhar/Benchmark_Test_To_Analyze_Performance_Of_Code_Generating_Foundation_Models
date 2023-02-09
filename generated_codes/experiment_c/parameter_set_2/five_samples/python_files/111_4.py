"""


"""

import re

def find_max(s):
    num = re.findall('[0-9]+', s)
    num = [int(i) for i in num]
    num.sort()
    return num[-1]

def main():
    s = input()
    print(find_max(s))

if __name__ == '__main__':
    main()