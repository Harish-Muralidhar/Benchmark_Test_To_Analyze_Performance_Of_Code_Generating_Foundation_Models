'''


'''

import math
testcase = int(input())
while(testcase > 0):
    n, k = map(int,input().split())
    #print(n,k)
    max_coin = math.ceil(n/k)
    print(max_coin)
    testcase -= 1