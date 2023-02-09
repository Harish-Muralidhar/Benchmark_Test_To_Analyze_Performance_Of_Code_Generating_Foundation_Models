"""

Tuzik can choose any number of people from 1 to K.

Hint
"""

# CODE
T = int(input())
for i in range(T):
    N,K = list(map(int, input().split()))
    print(N//K)