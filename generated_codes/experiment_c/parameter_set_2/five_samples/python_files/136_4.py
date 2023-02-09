'''


'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def nCr(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

def solve(n,k):
    if n == 1:
        return k
    else:
        return (k-1) * solve(n-1,k)

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    print(solve(n,k)%(10**9+7))