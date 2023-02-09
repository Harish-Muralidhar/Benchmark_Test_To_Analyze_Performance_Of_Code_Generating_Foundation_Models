'''


Explanation

In the first test case, the beanstalk has exactly one stem at level 1, and it branches into two stems at level 2, each of which ends in a leaf.

In the second test case, the beanstalk has exactly one stem at level 1, and it branches into two stems at level 2, but only one of them ends in a leaf. This is not possible.

'''

import math

def is_possible(n):
    if n == 0:
        return True
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return is_possible(n/2)
    else:
        return is_possible(n-1) or is_possible(n+1)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        if is_possible(sum(l)):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()