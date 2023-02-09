"""



Explanation
In the first test case, the given comparisons are consistent. So, we can distribute bonus among them. The minimum total bonus is 460$. To achieve this, employee 1 can get 140$, employee 2 can get 120$, employee 3 can get 100$, and employee 4 can get 100$.
In the second test case, the given comparisons are inconsistent. So, we can’t distribute bonus among them.

"""

import sys

def main():
    num_test_cases = int(sys.stdin.readline())
    for i in range(num_test_cases):
        num_employees, num_comparisons, min_bonus = map(int, sys.stdin.readline().split())
        comparisons = []
        for j in range(num_comparisons):
            comparisons.append(list(map(int, sys.stdin.readline().split())))
        print(comparisons)

if __name__ == '__main__':
    main()