'''

Explanation :

In case 3, 3*2*1 = 6

In case 4, 4*3*2*1 = 24

In case 5, 5*4*3*2*1 = 120

'''
# your code goes here

T = int(input())

for i in range(T):
    N = int(input())
    s = 1
    for j in range(1,N+1):
        s = s*j
    
    print(s)