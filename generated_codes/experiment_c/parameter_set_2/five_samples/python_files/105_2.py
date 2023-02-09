"""


Explanation
The first case is explained in the question. The second case is a special case where the number has only one block. So, the flag is set to 1 and the binary number is 1.

"""

import sys

def main():
    flag = 1
    for line in sys.stdin:
        if line == '~\n':
            break
        line = line.strip()
        if line == '#':
            print(int(bin(int(flag)), 2))
            flag = 1
            continue
        if len(line) == 1:
            flag = 1
            continue
        elif len(line) == 2:
            flag = 0
            continue
        else:
            flag = bin(int(flag))[2:]
            flag = flag * (len(line) - 2)
            flag = int(flag, 2)

if __name__ == "__main__":
    main()