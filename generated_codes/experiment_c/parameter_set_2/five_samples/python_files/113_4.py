'''

'''

def is_fib(n):
    phi = 0.5 + 0.5 * 5 ** 0.5
    a = phi * n
    return n == 0 or abs(round(a) - a) < 1.0 / n

for _ in range(int(input())):
    n = int(input())
    if is_fib(n):
        print("YES")
    else:
        print("NO")