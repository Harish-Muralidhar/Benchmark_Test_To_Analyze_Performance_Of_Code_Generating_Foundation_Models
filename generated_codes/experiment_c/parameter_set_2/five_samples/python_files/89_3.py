"""

Explanation

The first line of the input means that there are 7 houses and 5 actions.
The second line means that CodeChef adds a system protecting houses 1 through 4.
The third line means that CodeChef adds another system protecting houses 3 through 5.
The fourth line means that the enemy bombs the 3-rd house. There are two systems protecting that house, so the output is 2.
The fifth line means that CodeChef moves the second system one house to the right.
The sixth line means that the enemy bombs the 3-rd house. There is only one system protecting that house, so the output is 1.

"""

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    sys_list = []
    for i in range(m):
        op = sys.stdin.readline().split()
        if op[0] == 'P':
            sys_list.append([int(op[1]), int(op[2])])
        elif op[0] == 'M':
            sys_list[int(op[1])-1][0] += int(op[2])
            sys_list[int(op[1])-1][1] += int(op[2])
        elif op[0] == 'B':
            count = 0
            for sys in sys_list:
                if sys[0] <= int(op[1]) <= sys[1]:
                    count += 1
            print(count)

if __name__ == "__main__":
    main()