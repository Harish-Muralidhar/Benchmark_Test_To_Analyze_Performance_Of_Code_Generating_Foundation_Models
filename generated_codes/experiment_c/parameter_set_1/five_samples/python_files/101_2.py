'''

The first example is the beanstalk described in the problem statement. The second beanstalk has level 1 leaves 0, level 2 leaves 0, and level 3 leaves 3, which is not possible, given the rules.


'''


def valid_beanstalks(k, num_leaves):
    if num_leaves[0] == 0:
        return True

    for i in range(k-1):
        if num_leaves[i] > 0:
            num_leaves[i+1] -= min(num_leaves[i], 1)
            num_leaves[i] -= min(num_leaves[i], 2)

    if num_leaves[-1] > 0:
        return False
    else:
        return True


if __name__ == '__main__':
    num_tests = int(input())
    for _ in range(num_tests):
        k = int(input())
        num_leaves = list(map(int, input().split()))
        print('Yes' if valid_beanstalks(k, num_leaves) else 'No')