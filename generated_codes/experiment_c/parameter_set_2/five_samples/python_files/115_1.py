"""

"""

import sys

def game(arr):
    while True:
        arr.sort()
        if arr[0] == arr[-1]:
            return arr[0]
        else:
            arr[-1] = arr[-1] - arr[0]

if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        arr = list(map(int, sys.stdin.readline().split()))
        print(game(arr))