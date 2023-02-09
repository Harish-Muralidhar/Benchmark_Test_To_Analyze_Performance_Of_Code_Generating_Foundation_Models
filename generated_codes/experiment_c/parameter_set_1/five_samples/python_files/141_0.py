'''

'''


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def combinations(n,k):
    n_fact = factorial(n)
    k_fact = factorial(k)
    n_sub_k_fact = factorial(n-k)
    return n_fact/(k_fact*n_sub_k_fact)

def solve(n,m):
    return combinations(n*m,2) - (n*m*(n*m - 1)/2)

for _ in range(int(input())):
    n,m = map(int,input().split())
    print(solve(n,m))