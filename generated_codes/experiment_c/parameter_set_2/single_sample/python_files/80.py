"""

"""

import sys
import re

def main():
    #read input
    input_lines = sys.stdin.readlines()
    #print(input_lines)
    #remove newlines
    input_lines = [line.strip() for line in input_lines]
    #print(input_lines)
    #remove first line
    input_lines = input_lines[1:]
    #print(input_lines)
    #split into list of lists
    input_lines = [line.split() for line in input_lines]
    #print(input_lines)
    #split product and size
    input_lines = [line[0].split('.') + line[1:] for line in input_lines]
    #print(input_lines)
    #split province, city and region
    input_lines = [line[:2] + line[2].split('.') + line[3:] for line in input_lines]
    #print(input_lines)
    #split age
    input_lines = [line[:5] + line[5].split('-') + line[6:] for line in input_lines]
    #print(input_lines)
    #convert to int
    input_lines = [[int(x) for x in line] for line in input_lines]
    #print(input_lines)
    #remove empty strings
    input_lines = [line for line in input_lines if line != []]
    #print(input_lines)

    #initialize dictionary
    d = {'I':[], 'Q':[]}
    #fill dictionary
    for line in input_lines:
        d[line[0]].append(line[1:])
    #print(d)

    #initialize dictionary
    d2 = {'I':{}, 'Q':{}}
    #fill dictionary
    for line in d['I']:
        d2['I'][(line[0], line[1], line[2], line[3])] = line[4]
    #print(d2)

    #initialize dictionary
    d3 = {'Q