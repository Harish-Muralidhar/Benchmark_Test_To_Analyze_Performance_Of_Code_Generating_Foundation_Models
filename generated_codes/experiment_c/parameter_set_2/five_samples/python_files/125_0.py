"""
Example case 2. Game will have 2 turns. In the first turn Sasha will choose 1, while Chef will choose 2. In the second turn Sasha will choose 4, while Chef will choose 3. Hence answer is 1.5.
Example case 3. Game will have 2 turns. In the first turn Sasha will choose 2, while Chef will choose 2. In the second turn Sasha will choose 2, while Chef will choose 4. In both cases x^y=y^x, hence Sasha will never kiss Chef. Hence answer is 0.

"""

import math

def expected_kisses(n, a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    count = 0
    while i < n and j < n:
        if a[i] < b[j]:
            count += math.pow(a[i], b[j])
            i += 1
        else:
            count += math.pow(b[j], a[i])
            j += 1
    return count


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(expected_kisses(n, a, b))