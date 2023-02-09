"""

"""

def sum_of_k_powers(n, k, p):
    sum = 0
    for i in range(1, n+1):
        sum += i**k
    return sum % p

t = int(input())
for i in range(t):
    n, k, p = map(int, input().split())
    print(sum_of_k_powers(n, k, p))