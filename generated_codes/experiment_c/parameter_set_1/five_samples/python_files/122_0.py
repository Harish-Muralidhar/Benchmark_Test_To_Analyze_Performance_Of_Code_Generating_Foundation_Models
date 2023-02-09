'''
'''

import math
def pi_approx(k):
    n = int(k)
    ans = ""
    if n == 0:
        return "3"
    ans = ans + "3."
    for i in range(1,n+1):
        ans = ans + str(int(math.floor(((10**(i-1))*(103993%33102))/33102)))
    return ans

T = int(input())
for _ in range(T):
    K = int(input())
    print(pi_approx(K))