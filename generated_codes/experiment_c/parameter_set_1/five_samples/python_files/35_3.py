'''



SOLUTION:
'''
T=int(input())
for i in range(0,T):
    N=int(input())
    fact=1
    for i in range(1,N+1):
        fact=fact*i
    print(fact)