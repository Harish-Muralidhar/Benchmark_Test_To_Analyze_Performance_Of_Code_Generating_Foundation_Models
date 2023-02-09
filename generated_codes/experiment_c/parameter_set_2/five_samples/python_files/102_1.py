"""
 = 100, nnn = 3, and nnn = 1.

"""


import sys

def read_input(file):
    with open(file) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def check_hints(hints):
    if hints[0][1] == '<':
        if hints[0][2] == 'Yes':
            return '1'
        else:
            return '0'
    elif hints[0][1] == '>':
        if hints[0][2] == 'Yes':
            return '0'
        else:
            return '1'
    else:
        if hints[0][2] == 'Yes':
            return '0'
        else:
            return '1'

def main():
    lines = read_input(sys.argv[1])
    test_cases = int(lines[0])
    for i in range(1, test_cases+1):
        hints = []
        hint_count = int(lines[i])
        for j in range(1, hint_count+1):
            hints.append(lines[i+j].split())
        print check_hints(hints)

if __name__ == '__main__':
    main()