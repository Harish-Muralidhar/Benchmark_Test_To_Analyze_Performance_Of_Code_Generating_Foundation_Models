'''

Explanation:

The first number contains 4 fours: 44, 474, 447, 477
The second number doesn't contain the digit 4.
The third number contains a single 4.
The fourth number contains a single 4.
The fifth number doesn't contain the digit 4.)

'''

#Solution 
import re
for i in range(int(input())):
    s = input()
    print(len(re.findall('4',s)))