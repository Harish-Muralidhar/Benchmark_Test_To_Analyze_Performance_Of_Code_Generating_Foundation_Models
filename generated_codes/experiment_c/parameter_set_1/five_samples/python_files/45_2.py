'''

Explanation
Example case 1. We have 'a' = 3 and 'b' = 1. 3 = 1 + 2 = 1 + 1 + 1.
Example case 2. We have 'z' = 4 and 'q' = 2. 4 = 2 + 2.
Example case 3. We have 'a' = 1, 'b' = 1 and 'c' = 1. 1 = 1 + 0 = 1 + 0 = 1 + 0.
Example case 4. We have 'k' = 3, 'l' = 1 and 'w' = 4. 3 = 4 - 1 = 1 + 1 + 1. 
'''

import collections

for _ in range(int(input())):
    a = input()
    dict_a = collections.Counter(a)
    if len(dict_a) == 1:
        print('YES')
    else:
        sum_a = sum(dict_a.values())
        sum_b = sum([abs(i) for i in dict_a.values()])
        if sum_a == sum_b:
            print('YES')
        else:
            print('NO')