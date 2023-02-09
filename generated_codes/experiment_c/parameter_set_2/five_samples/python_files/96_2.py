'''

'''

import sys

def get_input(file):
    f = open(file, 'r')
    return f.read()

def get_candies(input):
    lines = input.splitlines()
    n = int(lines[0])
    candies = []
    for i in range(1, n+1):
        candies.append(lines[i].split(' '))
    return candies

def get_desired_ratio(input):
    lines = input.splitlines()
    return lines[-1].split(' ')

def get_ratio(candies, desired_ratio):
    for candy in candies:
        candy.append(float(candy[0])/float(candy[1]))
    desired_ratio.append(float(desired_ratio[0])/float(desired_ratio[1]))
    return candies, desired_ratio

def get_candies_to_buy(candies, desired_ratio):
    candies_to_buy = []
    for candy in candies:
        if candy[2] == desired_ratio[2]:
            candies_to_buy.append(candy)
    if candies_to_buy:
        return candies_to_buy
    else:
        return -1

def get_min_candies_to_buy(candies, desired_ratio):
    candies_to_buy = get_candies_to_buy(candies, desired_ratio)
    if candies_to_buy == -1:
        return -1
    else:
        min_candies_to_buy = sys.maxint
        for candy in candies_to_buy:
            if int(candy[0]) < min_candies_to_buy:
                min_candies_to_buy = int(candy[0])
        return min_candies_to_buy

def main():
    input = get_input('input.txt')
    candies = get_candies(input)
    desired_ratio