"""
 = 1, 2, and 3.

"""

import sys

def main():
    # Read the input
    t = int(sys.stdin.readline())
    while t:
        k = int(sys.stdin.readline())
        left = 1
        right = 10**9
        lies = 0
        for i in range(k):
            line = sys.stdin.readline().split()
            operator = line[0]
            li = int(line[1])
            logical_value = line[2]
            if operator == '<':
                if logical_value == 'Yes':
                    left = max(left, li+1)
                else:
                    right = min(right, li)
            elif operator == '>':
                if logical_value == 'Yes':
                    right = min(right, li-1)
                else:
                    left = max(left, li)
            else:
                if logical_value == 'Yes':
                    left = max(left, li)
                    right = min(right, li)
                else:
                    lies += 1
        print(lies)
        t -= 1

if __name__ == '__main__':
    main()