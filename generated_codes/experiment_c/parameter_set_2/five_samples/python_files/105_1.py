"""


Explanation
The first number is equivalent to binary 11011 which is 27 in decimal. The second number is equivalent to binary 1 which is 1 in decimal.

"""

import sys

def main():
    # read the input
    input_lines = sys.stdin.readlines()
    # remove the trailing newline character
    input_lines = [line.rstrip() for line in input_lines]
    # remove the last element, which is the '~' character
    input_lines = input_lines[:-1]
    # the input is a list of strings, so we need to join them
    input_string = ''.join(input_lines)
    # split the input string into a list of strings, where each string is a block
    input_blocks = input_string.split()
    # initialize the flag variable
    flag = 0
    # initialize the binary number
    binary_number = ''
    # iterate over the blocks
    for block in input_blocks:
        # if the block has 2 characters, then it has 2 zeros
        if len(block) == 2:
            flag = 0
        # if the block has 1 character, then it has 1 zero
        elif len(block) == 1:
            flag = 1
        # if the block has more than 2 characters, then it has more than 2 zeros
        else:
            # append the flag n-2 times to the binary number
            binary_number += flag * (len(block) - 2)
    # convert the binary number to decimal
    decimal_number = int(binary_number, 2)
    # print the decimal number
    print(decimal_number)

if __name__ == '__main__':
    main()