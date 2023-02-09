'''
 

Explanation:

In the first test case 10*10=100. The square root of 100 is 10. In the second test case 5*5=25. The square root of 25 is 5. In the third test case 10000*10000=100000000. The square root of 100000000 is 10000.

'''

import math

t = int(input())

while(t>0):
    n = int(input())
    print(math.sqrt(n))
    t = t-1