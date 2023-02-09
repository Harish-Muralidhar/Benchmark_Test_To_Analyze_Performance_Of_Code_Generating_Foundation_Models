'''

In the second example, Chef can choose any Secret Digit from 0 to 9. But you can only open page with numbers 1, 2, 3, 4, 5. Probability that the Secret Digit is 1, 2, 3, 4, 5 after you opened one of the pages 1, 2, 3, 4, 5 is 1/10.

'''
import random
T=int(input())
while T>0:
    N=int(input())
    S=random.randint(0,9)
    P=N-1
    if N==1:
        P=1
    print(P,"/10")
    T-=1