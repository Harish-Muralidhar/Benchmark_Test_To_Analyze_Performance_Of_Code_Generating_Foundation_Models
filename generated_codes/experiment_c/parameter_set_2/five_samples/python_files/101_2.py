'''


Explanation

In the first test case, the beanstalk has 0 leaves at level 1, 1 leaf at level 2 and 2 leaves at level 3. This is a possible growth of a beanstalk.

In the second test case, the beanstalk has 0 leaves at level 1 and level 2, and 3 leaves at level 3. This is impossible, because at level 2 there must be at least one leaf.

'''

import math

def is_possible(n):
    if n == 1:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False

def is_possible_leaf(n):
    if n == 0:
        return True
    if n == 1:
        return False
    if n % 2 == 0:
        return is_possible(n / 2)
    else:
        return is_possible(n)

def is_possible_beanstalk(levels):
    for i in range(1, len(levels)):
        if not is_possible_leaf(levels[i]):
            return False
    return True

def main():
    t = int(input())
    for _ in range(t):
        k = int(input())
        levels = list(map(int, input().split()))
        assert(len(levels) == k)
        print('Yes' if is_possible_beanstalk(levels) else 'No')

if __name__ == '__main__':
    main()