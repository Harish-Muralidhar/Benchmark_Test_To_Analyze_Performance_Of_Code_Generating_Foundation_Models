'''

'''

def is_fibonacci(n):
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    if n in fib:
        return True
    else:
        return False

t = int(input())
for i in range(t):
    n = int(input())
    if is_fibonacci(n):
        print("YES")
    else:
        print("NO")