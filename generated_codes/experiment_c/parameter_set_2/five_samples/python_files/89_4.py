'''

Explanation

At the beginning, there are two systems:

The first system protects houses 1 through 4.
The second system protects houses 3 through 5.
The enemy bombs the 3rd house.
There are two systems protecting the 3rd house: the first system and the second system.
CodeChef moves the second system by 1 house.
The second system now protects houses 4 through 6.
The enemy bombs the 3rd house.
There is only one system protecting the 3rd house: the first system.

'''

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    systems = []
    for i in range(m):
        line = sys.stdin.readline().split()
        if line[0] == 'P':
            systems.append((int(line[1]), int(line[2])))
        elif line[0] == 'M':
            systems[int(line[1])-1] = (systems[int(line[1])-1][0]+int(line[2]), systems[int(line[1])-1][1]+int(line[2]))
        elif line[0] == 'B':
            count = 0
            for system in systems:
                if system[0] <= int(line[1]) <= system[1]:
                    count += 1
            print(count)

if __name__ == '__main__':
    main()