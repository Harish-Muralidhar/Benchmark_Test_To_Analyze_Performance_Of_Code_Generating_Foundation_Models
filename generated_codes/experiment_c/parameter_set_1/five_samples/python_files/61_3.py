"""

All subtasks: 1 <= N <= 10^5.

"""

def sum_and(lst):
    """
    Returns the sum of AND of all the pairs of numbers in the given list.
    """
    total = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i < j:
                total += lst[i] & lst[j]
    return total

if __name__ == "__main__":
    N = int(input())
    lst = [int(x) for x in input().split()]
    print(sum_and(lst))