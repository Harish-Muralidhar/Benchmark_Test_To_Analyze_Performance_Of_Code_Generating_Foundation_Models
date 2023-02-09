'''
 pairs.
Case 4 : N = 6. Arjuna can make the pair (1,4). Bhima can not make any more pairs ( without crossing the pair (1,4) )

'''

'''
Solution:

We can observe that the person who starts the game, always wins.

Let's assume that the person who starts the game, loses.

Let's say the person who starts the game, makes a pair (a,b).

Now, the other person can make a pair (c,d) such that (a,b) and (c,d) do not cross each other.

Now, the first person can make a pair (e,f) such that (c,d) and (e,f) do not cross each other.

And this continues, and the first person can always make a pair.

So, the person who starts the game, always wins.

'''

#code

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def winner(n):
    if n == 2:
        return "Arjuna"
    if is_prime(n):
        return "Arjuna"
    return "Bhima"

t = int(input())
for i in range(t):
    n = int(input())
    print(winner(n))