'''


'''

import sys
from collections import defaultdict

def get_ways(n, dp):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in dp:
        return dp[n]
    dp[n] = get_ways(n-1, dp) + get_ways(n-2, dp)
    return dp[n]

def get_ways_with_obstacles(n, dp, obstacles):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in dp:
        return dp[n]
    if n in obstacles:
        return 0
    dp[n] = get_ways_with_obstacles(n-1, dp, obstacles) + get_ways_with_obstacles(n-2, dp, obstacles)
    return dp[n]

def get_good_numbers(l, r):
    dp = defaultdict(int)
    good_numbers = []
    for i in range(l, r+1):
        if get_ways(i, dp) == i:
            good_numbers.append(i)
    return good_numbers

def get_good_numbers_with_obstacles(l, r, obstacles):
    dp = defaultdict(int)
    good_numbers = []
    for i in range(l, r+1):
        if get_ways_with_obstacles(i, dp, obstacles) == i:
            good_numbers.append(i)
    return good_numbers

def get_path(n, dp, obstacles):
    if n == 0:
        return '.'
    if n == 1:
        return '.'
    if n == 2:
        return '..'
    if n in dp:
        return dp[n]
    if n in obstacles:
        return ''
