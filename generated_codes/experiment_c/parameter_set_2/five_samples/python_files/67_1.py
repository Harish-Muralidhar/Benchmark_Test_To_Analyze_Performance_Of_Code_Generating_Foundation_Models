"""

"""

import sys
import os
import math
import heapq
import random
import string
import time

def read_input():
    """
    Reads input from stdin and returns a list of integers
    """
    return sys.stdin.readline().strip().split(' ')

def read_int():
    """
    Reads input from stdin and returns an integer
    """
    return int(sys.stdin.readline().strip())

def read_int_array():
    """
    Reads input from stdin and returns an integer array
    """
    return [int(x) for x in sys.stdin.readline().strip().split(' ')]

def read_str_array():
    """
    Reads input from stdin and returns a string array
    """
    return [x for x in sys.stdin.readline().strip().split(' ')]

def read_float_array():
    """
    Reads input from stdin and returns a float array
    """
    return [float(x) for x in sys.stdin.readline().strip().split(' ')]

def read_float():
    """
    Reads input from stdin and returns a float
    """
    return float(sys.stdin.readline().strip())

def read_str():
    """
    Reads input from stdin and returns a string
    """
    return sys.stdin.readline().strip()

def read_int_matrix(n, m):
    """
    Reads input from stdin and returns a nxm matrix
    """
    matrix = []
    for i in range(n):
        matrix.append(read_int_array())
    return matrix

def read_float_matrix(n, m):
    """
    Reads input from stdin and returns a nxm float matrix
    """
    matrix = []
    for i in range(n):
        matrix.append(read_float_array())
    return matrix

def read_str_matrix(n, m):
    """
    Reads input from stdin