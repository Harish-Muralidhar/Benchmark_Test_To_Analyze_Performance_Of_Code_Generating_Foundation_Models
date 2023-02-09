"""

Explanation

Initially, there are two systems:

System 1 protects houses 1 through 4.
System 2 protects houses 3 through 5.

After the second command, system 2 is moved to protect houses 4 through 6.

After the third command, the enemy bombs the 3rd house. There are two systems protecting that house: system 1 and system 2.

After the fourth command, the enemy bombs the 3rd house again. There is only one system protecting that house: system 2.

"""

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    houses = [0] * (n+1)
    for i in range(m):
        command = sys.stdin.readline().split()
        if command[0] == 'P':
            for j in range(int(command[1]), int(command[2])+1):
                houses[j] += 1
        elif command[0] == 'M':
            for j in range(int(command[2]), int(command[2])+int(command[1])):
                houses[j] += 1
        elif command[0] == 'B':
            print(houses[int(command[1])])

if __name__ == '__main__':
    main()