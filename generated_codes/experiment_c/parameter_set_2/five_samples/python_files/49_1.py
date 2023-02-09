'''

Test 2 :  Chef will make 2 moves: pick up the first two elements (4 and 2), remove the larger one (4), incurring a cost equal to the smaller one (2). Then pick up the last two elements (2 and 5), remove the larger one (5), incurring a cost equal to the smaller one (2). The total cost will be 2+2 = 4.

'''

import sys

def min_cost(arr):
    cost = 0
    while len(arr) > 1:
        arr.sort()
        cost += arr[0]
        arr.pop(0)
        arr.pop(0)
    return cost

def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        arr = list(map(int, sys.stdin.readline().strip().split()))
        print(min_cost(arr))

if __name__ == '__main__':
    main()