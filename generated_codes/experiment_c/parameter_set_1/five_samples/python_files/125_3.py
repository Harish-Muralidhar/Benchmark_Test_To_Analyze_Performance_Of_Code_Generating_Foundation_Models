/*
Example case 2. Game will have 2 turns. In first turn, Chef will choose 2 and Sasha will choose 1. In second turn, Chef will choose 3 and Sasha will choose 4. Answer is 2/4+3/4=1.5.
 

*/

import sys
import random
 
T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(s) for s in input().split(" ")]
    B = [int(s) for s in input().split(" ")]
    sasha = 0
    for i in range(N):
        X = random.choice(A)
        Y = random.choice(B)
        if X**Y > Y**X:
            sasha += 1
        A.remove(X)
        B.remove(Y)
    print(sasha/N)