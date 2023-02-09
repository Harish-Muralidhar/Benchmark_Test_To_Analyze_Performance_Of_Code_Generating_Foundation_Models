"""




"""

import sys

def get_input():
    # Read the input from stdin and return it
    lines = sys.stdin.readlines()
    return lines

def parse_input(lines):
    # Parse the input into a list of lists
    # Each sublist contains the number of locations and the two permutations
    # For example, [[3, [1, 0, 2], [2, 1, 0]], [4, [0, 2, 1, 3], [1, 2, 3, 0]]]
    input_list = []
    for i in range(1, len(lines), 3):
        n = int(lines[i])
        s = [int(x) for x in lines[i+1].split()]
        t = [int(x) for x in lines[i+2].split()]
        input_list.append([n, s, t])
    return input_list

def solve(input_list):
    # Solve each test case and return the answers in a list
    answers = []
    for input in input_list:
        n = input[0]
        s = input[1]
        t = input[2]
        # Create a dictionary with keys 0 to n-1 and values 0
        d = {i: 0 for i in range(n)}
        # Create a list with n zeroes
        ds = [0] * n
        dt = [0] * n
        # For each location in s, increment the value of the dictionary
        # corresponding to the location
        for i in range(n):
            d[s[i]] += 1
            ds[i] = d[s[i]]
        # Reset the dictionary to all zeroes
        d = {i: 0 for i in range(n)}
        # For each location in t, increment the value of the dictionary
        # corresponding to the location
        for i in range(n):
            d[t[i]] += 1
            dt[i] = d[t[i]]
        # Find the maximum difference between the number of As and Bs
        # in