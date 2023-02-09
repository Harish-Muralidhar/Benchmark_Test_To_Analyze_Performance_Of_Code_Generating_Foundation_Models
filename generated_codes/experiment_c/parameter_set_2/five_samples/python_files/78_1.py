'''

Explanation

In the example, there are no rocks, so your cannon can successfully fire at the two guns at (-2, 2) and (-1, 2).

'''

import math

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return False
        return True

def is_rock(x, y):
    return is_prime(x) and is_prime(y)

def main():
    t = int(input())
    for i in range(t):
        y, x1, x2 = map(int, input().split())
        count = 0
        for x in range(x1, x2+1):
            if not is_rock(x, y):
                count += 1
        print(count)

if __name__ == '__main__':
    main()