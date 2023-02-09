'''

'''

import sys

def main():
    num_candies = int(sys.stdin.readline())
    candies = []
    for i in range(num_candies):
        candies.append(list(map(int, sys.stdin.readline().split())))
    desired = list(map(int, sys.stdin.readline().split()))
    # print(candies)
    # print(desired)
    num_candies_to_buy = 0
    for i in range(num_candies):
        for j in range(i+1, num_candies):
            if (candies[i][0]/candies[i][1]) != (candies[j][0]/candies[j][1]):
                if (candies[i][0]/candies[i][1]) == (desired[0]/desired[1]):
                    num_candies_to_buy += 1
                elif (candies[j][0]/candies[j][1]) == (desired[0]/desired[1]):
                    num_candies_to_buy += 1
                else:
                    num_candies_to_buy += 2
    if num_candies_to_buy == 0:
        print(-1)
    else:
        print(num_candies_to_buy)

if __name__ == '__main__':
    main()