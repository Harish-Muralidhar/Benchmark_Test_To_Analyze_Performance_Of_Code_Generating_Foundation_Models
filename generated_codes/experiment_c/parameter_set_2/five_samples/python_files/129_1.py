"""

Explanation

In the first test case, the atoms are {0,1,2}, {3}, and {4}.

In the second test case, the atoms are {0}, {1}, {2}, and {3}.

"""

import sys

def main():
    """
    Main function
    """
    test_cases = int(sys.stdin.readline())
    for _ in range(test_cases):
        n, m = map(int, sys.stdin.readline().split())
        sets = []
        for _ in range(m):
            sets.append(set(map(int, sys.stdin.readline().split()[1:])))
        print(solve(n, sets))

def solve(n, sets):
    """
    Solve the problem
    """
    sets = sorted(sets, key=lambda x: len(x))
    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            sets[j] -= sets[i]
    return len(sets)

if __name__ == '__main__':
    main()