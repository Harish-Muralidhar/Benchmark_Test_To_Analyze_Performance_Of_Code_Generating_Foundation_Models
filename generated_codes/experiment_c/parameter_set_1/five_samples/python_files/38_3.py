'''

Explanation:

In the first test case 10^1/2 = 3.16228 
In the second test case 5^1/2 = 2.23607 
In the third test case 10000^1/2 = 100
'''


import math
T = int(input())
for i in range(T):
    N = int(input())
    print(int(math.sqrt(N)))