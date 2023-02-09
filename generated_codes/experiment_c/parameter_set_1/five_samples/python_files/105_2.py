"""




Sample Input

0 "cmtt-10x-x-109">0000 00
000 "cmtt-10x-x-109">0 0000
#
0 "cmtt-10x-x-109">000 #
~

Sample Output

27
1

Explanation

First number is equivalent to binary 11011. So its decimal equivalent is 27. 
Second number is equivalent to binary 110. So its decimal equivalent is 1.

"""

# import the libraries
import sys

# initialize the input
input = sys.stdin.readlines()

# initialize the output
output = []

# initialize the flag
flag = 1

# define the function to covert the number from binary string to decimal integer
def binary_to_decimal(binary):
    return int(binary, 2)

# iterate each line in the input
for line in input:
    # initialize the output for the current line
    line_output = ''
    # iterate each char in the line
    for char in line:
        # if the char is '0'
        if char == '0':
            # if the flag is 0
            if flag == 0:
                # add the char to the line output
                line_output = line_output + '0'
            # if the flag is 1
            elif flag == 1:
                # change the flag to 0
                flag = 0
                # add the char to the line output
                line_output = line_output + '1'
        # if the char is '#'
        elif char == '#':
            # append the line output to the output
            output.append(binary_to_decimal(line_output))
            # break the loop
            break
        # if the char is ' '
        elif char == ' ':
            # if the flag is 0
            if flag == 0:
                # change the flag to 1
                flag = 1
            # if the flag is 1
            elif flag == 1:
                # add the char to the line output
                line_output = line_output + '1'
        # otherwise
        else:
            # if the flag is 0
            if flag == 0:
                # change the flag to 1
                flag = 1
                # add the char to the line output
                line_output = line_output + '1'
            # if the flag is 1
            elif flag == 1:
                # change the flag to 0
                flag = 0
                # add the char to the line output
                line_output = line_output + '1'
                line_output = line_output + char * (int(char) - 2)

# iterate each item in the output
for item in output:
    # print the item
    print(item)