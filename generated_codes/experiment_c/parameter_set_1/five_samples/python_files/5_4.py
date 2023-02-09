"""

"""

import re

test = int(input())

for i in range(test):
    length_n = int(input())
    seq_n = input().split()
    length_f = int(input())
    seq_f = input().split()

    seq_n = ''.join(seq_n)
    seq_f = ''.join(seq_f)

    if re.findall(seq_f, seq_n):
        print("Yes")
    else:
        print("No")