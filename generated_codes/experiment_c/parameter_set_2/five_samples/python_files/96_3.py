'''

'''

import math

def main():
    n = int(input())
    candies = []
    for i in range(n):
        candies.append([int(x) for x in input().split()])
    desired = [int(x) for x in input().split()]
    candies.sort(key=lambda x: x[0]/x[1])
    #print(candies)
    if desired[0]/desired[1] < candies[0][0]/candies[0][1]:
        print(-1)
        return
    if desired[0]/desired[1] > candies[-1][0]/candies[-1][1]:
        print(-1)
        return
    for i in range(len(candies)-1):
        if candies[i][0]/candies[i][1] < desired[0]/desired[1] < candies[i+1][0]/candies[i+1][1]:
            #print(candies[i], candies[i+1])
            if candies[i][0]/candies[i][1] < desired[0]/desired[1] < candies[i+1][0]/candies[i+1][1]:
                if candies[i][0]/candies[i][1] < desired[0]/desired[1] < candies[i+1][0]/candies[i+1][1]:
                    if candies[i][0]/candies[i][1] < desired[0]/desired[1] < candies[i+1][0]/candies[i+1][1]:
                        if candies[i][0]/candies[i][1] < desired[0]/desired[1] < candies[i+1][0]/candies[i+1][1]:
                            if candies[i][0]/candies[i][1] < desired[0]/desired[1] < candies[i+1][0]/candies[i