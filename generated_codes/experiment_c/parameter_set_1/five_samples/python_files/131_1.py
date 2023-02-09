"""


"""

def money_division(M, p):
    total = 0
    for t in range(0, M):
        total = total + (10**9)*(p**t)
    return total

T = int(input())
for t in range(T):
    M, p = input().split()
    M = int(M)
    p = float(p)
    print(money_division(M, p))