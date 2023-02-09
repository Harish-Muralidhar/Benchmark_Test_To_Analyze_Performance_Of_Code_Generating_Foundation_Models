"""

Explanation:
In the first test case 10*10=100. The square root of 100 is 10. In the second test case 5*5=25. The square root of 25 is 5. In the third test case 10000*10000=100000000. The square root of 100000000 is 10000.

Solution:

"""

import math

for i in range(int(input())):
    print(math.floor(math.sqrt(int(input()))))