"""
In the third case they are (4,4), (2,6), (2,2,2), (1,1,1,1), (1,3,3), (1,1,3), (1,1,1,3), (1,1,1,1,3) and (3,3,3).
"""

#code:
for i in range(int(input())):
    k, n = map(int, input().split())

    #base case:
    is_base = False
    if n in range(k):
        is_base = True
    if n == k:
        n = n - 1
        is_base = True

    #general case:
    k = k - 1
    p = 1
    q = 1
    for i in range(k):
        p = (p*(n-i))%1000000009
        q = (q*(i+1))%1000000009

    if is_base:
        p = (p*(n-k))%1000000009

    q = pow(q,1000000005,1000000009)
    ans = (p*q)%1000000009
    print(ans)