'''

Solution:

import math
from functools import reduce

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcmm(*args):
    return reduce(lcm, args)

n,k=map(int,input().split())
l=list(map(int,input().split()))
a=[]
for i in range(n-k):
    a.append(l[i])
for i in range(n-k+1,n):
    a.append(l[i])
print(lcmm(*a)%1000000007)

'''

# Question 2:

'''
Write a python code for the following question.
Import the necessary libraries.
Chef has a binary tree. The binary tree consists of 1..N nodes with the following properties:

Each node has a unique number assigned to it from the range [1..N].
Each node has up to two children, which are identified by their node numbers.
Each node is colored either red or black.
The root node is always colored black.
All leaf nodes are always colored red.
If a node is red, then both of its children are black.
The number of black nodes on the path from the root node to any leaf node is the same.
Chef has to perform Q operations of the following types:

C X Y: Chef colors the edge between nodes X and Y red.
Q X Y: Chef has to find the number of black nodes on the path between nodes X and Y.
Note: The path between X and Y doesn't contain X and Y.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and Q.
The second line contains N space-separated integers p1,p2,…,pN. For each valid i, the i-th of these integers denotes the color of the i-th node.
Each of