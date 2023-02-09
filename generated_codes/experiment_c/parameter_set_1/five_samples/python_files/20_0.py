'''

'''

import sys

#Read Number of test case
T=int(input())

#Read Each Line
for i in range(T):
    A,B=map(int,sys.stdin.readline().split())
    print(A+B)