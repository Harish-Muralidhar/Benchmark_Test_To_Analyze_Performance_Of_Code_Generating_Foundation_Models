"""
"""

import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if i == 0:
            print(1, end=" ")
        else:
            if arr[i] * arr[i - 1] < 0:
                print(i + 1, end=" ")
            else:
                print(1, end=" ")
    print()