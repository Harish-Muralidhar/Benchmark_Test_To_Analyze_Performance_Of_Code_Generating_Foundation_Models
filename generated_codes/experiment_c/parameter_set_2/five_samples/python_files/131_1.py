"""

"""

# SOLUTION

for _ in range(int(input())):
    m,p=map(float,input().split())
    print(1000000000*p**(m-1),1000000000*(1-p**(m-1)))