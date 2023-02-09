"""
"""

def fact(n):
    if n<0:
        return None
    elif n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

def zeros(n):
    z = 0
    while n>=5:
        z += (n//5)
        n = n//5
    return z

t = int(input())
for i in range(t):
    n = int(input())
    print(zeros(n))