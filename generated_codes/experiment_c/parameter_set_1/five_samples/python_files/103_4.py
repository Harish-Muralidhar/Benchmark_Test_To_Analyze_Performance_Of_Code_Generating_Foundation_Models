'''

Explanation
For the first test case, the answer is 4^4 = 256. The first two digits are 25 and the last two are 56.
For the second test case, the answer is 9^9 = 387420489. The first three digits are 387 and the last three are 489.
Note that there is no blank line between two consecutive test cases.

'''
import math
t = int(input())
ans = []
for i in range(t):
    n,k = list(map(int,input().split()))
    a = math.pow(n,n)
    a = str(a)
    a = a.replace('.','')
    print(a)
    b = len(a)-k

    print(a[0:k],a[b:len(a)])