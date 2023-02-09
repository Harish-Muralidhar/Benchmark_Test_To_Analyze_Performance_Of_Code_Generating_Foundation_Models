'''
Example case 2. Game will have 2 turns. In first turn Sasha will choose 2, while Chef will choose 3. Since 2^3<3^2 Sasha won't kiss boy. In second turn Sasha will choose 4, while Chef will choose 1. Since 4^1>1^4 Sasha will kiss boy. Hence answer is 1.5. 
Example case 3. Game will have 2 turns. In first turn Sasha will choose 2, while Chef will choose 2. Since 2^2=2^2 Sasha won't kiss boy. In second turn Sasha will choose 2, while Chef will choose 2. Since 2^2=2^2 Sasha won't kiss boy. Hence answer is 0.

'''

import random

def expected_kisses(n, a, b):
    a = sorted(a)
    b = sorted(b)
    count = 0
    for i in range(n):
        if a[i] ** b[i] > b[i] ** a[i]:
            count += 1
    return count

def expected_kisses_random(n, a, b):
    a = sorted(a)
    b = sorted(b)
    count = 0
    for i in range(n):
        x = random.choice(a)
        y = random.choice(b)
        if x ** y > y ** x:
            count += 1
    return count

def expected_kisses_random_2(n, a, b):
    count = 0
    for i in range(n):
        x = random.choice(a)
        y = random.choice(b)
        if x ** y > y ** x:
            count += 1
    return count

def expected_kisses_random_3(n, a, b):
    count = 0
    for i in range(n):
        x = random.choice(a)
        y = random.choice(b)
        if x ** y > y ** x:
            count += 1
    return count

def expected_kisses_random_4(n, a, b):
    count = 0
    for i in range(n):
        x = random.choice(a