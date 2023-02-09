'''

Solution:

'''

import re

S = input()
max_num = -1

for num in re.findall(r'\d+', S):
    max_num = max(max_num, int(num))

print(max_num)