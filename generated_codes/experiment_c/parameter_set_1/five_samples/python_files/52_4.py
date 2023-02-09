'''
The fractions will be given in the form a_k/b_k.



Explanation :

In the first test case, the maximum fraction you can get by starting at index 1 is 1/1 + 4/3 + 10/1 = 3/1. Similarly, the maximum fraction you can get by starting at index 2 is 4/3 + 10/1 = 7/2
'''

import fractions

T = int(input())

for _ in range(T):
    N = int(input())
    num = []
    denom = []
    for i in range(N):
        a, b = input().split('/')
        num.append(int(a))
        denom.append(int(b))

    res_num = num.copy()
    res_denom = denom.copy()
    for i in range(N - 2, -1, -1):
        res_num[i] = num[i] + res_num[i + 1]
        res_denom[i] = denom[i] + res_denom[i + 1]

    for i in range(N):
        res = fractions.Fraction(res_num[i], res_denom[i])
        print(res.numerator, res.denominator)
    print()