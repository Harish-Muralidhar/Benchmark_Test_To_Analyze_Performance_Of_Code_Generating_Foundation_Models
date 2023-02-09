"""

"""

import sys

def check_beanstalk(list_of_leaves):
    for i in range(1,len(list_of_leaves)):
        if list_of_leaves[i] > list_of_leaves[i-1] + 2:
            return False
        else:
            return True

def main():
    t = int(input())
    for i in range(t):
        levels = int(input())
        list_of_leaves = [int(i) for i in sys.stdin.readline().split()]
        print('Yes' if check_beanstalk(list_of_leaves) else 'No')


if __name__ == '__main__':
    main()