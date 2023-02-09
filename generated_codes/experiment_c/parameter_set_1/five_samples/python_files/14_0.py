"""
 

Note
The first test case is already satisfied, so answer is 0.
In the second test case, 2 is not a power of 2, so divide it by 2 and get 1, then multiply this number by 2 four times, and get 16. This is done in 4 operations, so the answer is 4.

Testcase 1
Sampling    Input   Output
1
1 1
0
"""
import math
for i in range(int(input())):
    A,B=map(int,input().split())
    if(A==B):
        print(0)
    else:
        if(A<B):
            print(int(math.log(B,2))-int(math.log(A,2)))
        else:
            print(int(math.log(A,2))-int(math.log(B,2)))