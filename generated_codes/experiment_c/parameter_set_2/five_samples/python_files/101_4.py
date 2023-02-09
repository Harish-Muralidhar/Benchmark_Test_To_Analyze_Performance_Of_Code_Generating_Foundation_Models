"""


Explanation

In the first test case, the leaf counts are correct. The beanstalk can grow in the following way:

Level 1: 1 stem, 0 leaves
Level 2: 1 stem, 1 leaf
Level 3: 1 stem, 2 leaves

In the second test case, the leaf counts are not correct. The beanstalk can grow in the following way:

Level 1: 1 stem, 0 leaves
Level 2: 1 stem, 0 leaves
Level 3: 2 stems, 3 leaves

However, the leaf counts at levels 1 and 2 are not correct.

"""

import sys

def is_possible(k, leaves):
    if leaves[0] > 1:
        return False
    for i in range(1, k):
        if leaves[i] > leaves[i-1]*2:
            return False
    return True

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        k = int(sys.stdin.readline())
        leaves = [int(x) for x in sys.stdin.readline().split()]
        if is_possible(k, leaves):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()