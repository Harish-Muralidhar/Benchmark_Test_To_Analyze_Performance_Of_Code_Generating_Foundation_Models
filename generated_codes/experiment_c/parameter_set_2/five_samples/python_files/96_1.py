"""

"""

import sys
import math

def main():
    N = int(input())
    candies = []
    for i in range(N):
        candies.append(list(map(int, input().split())))
    desired = list(map(int, input().split()))
    candies.sort(key=lambda x: x[1]/x[0])
    desired_ratio = desired[1]/desired[0]
    min_candies = sys.maxsize
    for i in range(N):
        if candies[i][1]/candies[i][0] > desired_ratio:
            break
        else:
            count = math.ceil(desired[0]/candies[i][0])
            if count < min_candies:
                min_candies = count
    if min_candies == sys.maxsize:
        print(-1)
    else:
        print(min_candies)

if __name__ == "__main__":
    main()