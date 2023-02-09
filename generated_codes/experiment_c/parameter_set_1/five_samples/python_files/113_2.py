'''

'''


def isFibo(num):
    a=0
    b=1
    i=0
    while i<num:
        i=a+b
        a=b
        b=i
    if i==num:
        return True
    else:
        return False
        
t=int(input())
for i in range(t):
    n=int(input())
    if isFibo(n):
        print("YES")
    else:
        print("NO")