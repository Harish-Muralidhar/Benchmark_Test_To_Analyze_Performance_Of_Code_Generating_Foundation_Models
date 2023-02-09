"""

"""

# Write your code here
from collections import deque
from math import log
from math import ceil
from pprint import pprint
from copy import copy

# MODULUS = 1000000009
MODULUS = 13

def get_parameters():
    test_cases = int(input())
    for i in range(test_cases):
        n,m = list(map(int,input().split()))
        data = list(map(int,input().split()))
        yield n,m,data


def get_pow_of_two(exponent):
    if exponent == 0:
        return 1
    return 2*get_pow_of_two(exponent-1)


def get_binary_representation(integer):
    binary_representation = ''
    while integer:
        integer,remainder = divmod(integer,2)
        binary_representation = str(remainder)+binary_representation
    return binary_representation

def get_max_sum(data):
    return sum(data)

def get_initial_bins(data, m, max_sum):
    binary_representation = get_binary_representation(max_sum)
    if len(binary_representation) <= m:
        return [data]
    return get_bins(data,m)

def is_valid_bin(bin_data, max_sum, m):
    binary_representation = get_binary_representation(max_sum)
    return binary_representation[-m-1] == '0'

def get_bins(data,m):
    if len(data) == 1:
        return [data]
    bins = []
    for i in range(len(data)-1):
        left_bin = data[:i+1]
        right_bin = data[i+1:]
        left_bins = get_bins(left_bin,m)
        right_bins = get_bins(right_bin,m)
        for left_bin in left_bins:
            for right_bin in right_bins:
                bins.append(left_bin+right_bin)
    return bins

def get_valid_bins(bins, m, max_sum):
    valid_bins = []
    for bin in bins:
        max_sum_bin = sum(bin)
        if is_valid_bin(bin, max_sum_bin, m):
            valid_bins.append(bin)
    return valid_bins

def get_number_of_ways_to_partition(data, m):
    max_sum = get_max_sum(data)
    bins = get_initial_bins(data, m, max_sum)
    valid_bins = get_valid_bins(bins, m, max_sum)
    pprint(valid_bins)
    return len(valid_bins)%MODULUS

def print_output(output):
    for i in output:
        print(i)

def main():
    output = []
    for n,m,data in get_parameters():
        output.append(get_number_of_ways_to_partition(data, m))
    print_output(output)

if __name__ == '__main__':
    main()