'''

'''

def is_fibonacci(n):
    a,b=0,1
    while a<=n:
        if a==n:
            return True
        a,b=b,a+b
    return False

for _ in range(int(input())):
    n=int(input())
    if is_fibonacci(n):
        print("YES")
    else:
        print("NO")