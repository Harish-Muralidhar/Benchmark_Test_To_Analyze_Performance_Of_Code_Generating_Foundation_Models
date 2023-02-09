'''

Explanation

In the first test case, the beanstalk has 0 leaves at the 1st level, 1 leaf at the 2nd level, and 2 leaves at the 3rd level, which is a valid growth.

In the second test case, the beanstalk has 0 leaves at the 1st level, 0 leaves at the 2nd level, and 3 leaves at the 3rd level, which is not a valid growth.

'''

import math

def canGrow(k,l):
    if k==0:
        return l==1
    for i in range(math.floor(math.log2(l))+1):
        if 2**i == l:
            return canGrow(k-1,l//2)
    return False


t = int(input())
for _ in range(t):
    k = int(input())
    l = list(map(int,input().split()))
    print('Yes' if canGrow(k,l[k-1]) else 'No')