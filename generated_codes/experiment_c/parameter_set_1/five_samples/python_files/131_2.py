'''

Example case 2. In the second case, it's better to divide the money equally, than to propose a plan worth more than 5*10^8 for Chef and less for the other guy.

Solution
'''

# cook your dish here
t = int(input())
while t!=0:
    t-=1
    x,p = map(float,input().split())
    print('%0.1f' % (1e9 * (1-p**x)/(1-p)),'%0.1f' % (1e9 * p**(x-1)))