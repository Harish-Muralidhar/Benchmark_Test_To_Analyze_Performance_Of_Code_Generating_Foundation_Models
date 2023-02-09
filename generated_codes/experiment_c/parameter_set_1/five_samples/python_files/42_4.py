'''

1. Input

n = 7
k = 3

[1, 51, 966369, 7, 9, 999999, 11]

2. Output

4

3. Approach

For every value in list, check if modulo k == 0

4. Solution

O(n)

5. Code

'''


def divisible_count(n, k, lst):
    """
    :param n: num
    :param k: divisor
    :param lst: list of potential divisible numbers
    """
    count = 0
    for i in lst:
        if i % k == 0:
            count += 1
    return count


if __name__ == "__main__":
    n, k = [int(i) for i in input().strip().split()]
    lst = [int(input()) for i in range(n)]
    print(divisible_count(n, k, lst))