"""
Example case 2. Game will have 2 turns. In first turn Sasha will choose 2, while Chef will choose 3. In second turn Sasha will choose 1, while Chef will choose 4. Hence answer is 1.5.
Example case 3. Sasha will always choose 2, while Chef will always choose 4. Since 2^4<4^2 girl will never kiss boy. Hence answer is 0.

"""

import random

def expected_kisses(n, a, b):
    """
    :param n: number of turns
    :param a: list of numbers given by Sasha
    :param b: list of numbers given by Chef
    :return: expected number of kisses
    """
    kisses = 0
    for i in range(n):
        x = random.choice(a)
        y = random.choice(b)
        if x**y > y**x:
            kisses += 1
        a.remove(x)
        b.remove(y)
    return kisses/n


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(expected_kisses(n, a, b))