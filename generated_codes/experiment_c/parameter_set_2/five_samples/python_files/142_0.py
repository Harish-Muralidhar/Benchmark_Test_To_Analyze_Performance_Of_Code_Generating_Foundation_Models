"""

"""

def solve(n, a, b):
    """
    :param n: Number of Bytelandians
    :param a: List of lower bounds
    :param b: List of upper bounds
    :return:
    """
    # Write your code here


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = []
        b = []
        for j in range(n):
            x, y = map(int, input().split())
            a.append(x)
            b.append(y)
        solve(n, a, b)