"""
"""

# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 13:19:12
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

nb_test = read_int()
for _ in range(nb_test):
    m, p = read_ints()
    print(1000000000 * (1-p) / (1 - (p**m)), 1000000000 * (1-p) / (1 - (p**m)))