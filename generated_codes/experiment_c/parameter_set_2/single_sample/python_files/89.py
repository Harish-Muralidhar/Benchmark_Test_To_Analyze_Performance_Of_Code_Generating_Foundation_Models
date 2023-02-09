'''

Explanation

The first system protects houses 1 through 4, and the second system protects houses 3 through 5.

After the second system is moved by 1 house, it protects houses 4 through 6.

'''

import sys

def main():
    # Read the input
    n, m = map(int, sys.stdin.readline().split())
    # Create a list of length n+1, with all elements set to 0
    house = [0] * (n+1)
    # For each of the m commands
    for i in range(m):
        # Read the command
        command = sys.stdin.readline().split()
        # If the command is to add a system
        if command[0] == "P":
            # Set all houses in the range to 1
            for j in range(int(command[1]), int(command[2])+1):
                house[j] = 1
        # If the command is to move a system
        elif command[0] == "M":
            # Set all houses in the range to 0
            for j in range(int(command[1]), int(command[2])+1):
                house[j] = 0
        # If the command is to bomb a house
        elif command[0] == "B":
            # Print the number of systems protecting the house
            print(house[int(command[1])])

if __name__ == "__main__":
    main()