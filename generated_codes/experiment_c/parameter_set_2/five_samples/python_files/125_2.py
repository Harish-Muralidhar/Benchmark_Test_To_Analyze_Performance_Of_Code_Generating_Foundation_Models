"""
Example case 2. Game will have 2 turns. In first turn Sasha will choose 2, and boy will choose 1. In second turn Sasha will choose 3, and boy will choose 4. Hence answer is 1 + 1.5 = 2.5 / 2 = 1.5.
Example case 3. In first turn Sasha will choose 2, and boy will choose 2. In second turn Sasha will choose 4, and boy will choose 2. Since 2^2 = 4^2, Sasha won't kiss boy. Hence answer is 0.

"""
import random

def expected_kisses(n, a, b):
    if n == 0:
        return 0
    x = random.choice(a)
    y = random.choice(b)
    a.remove(x)
    b.remove(y)
    if x**y > y**x:
        return 1 + expected_kisses(n-1, a, b)
    else:
        return 0 + expected_kisses(n-1, a, b)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(expected_kisses(n, a, b)/n)

if __name__ == '__main__':
    main()