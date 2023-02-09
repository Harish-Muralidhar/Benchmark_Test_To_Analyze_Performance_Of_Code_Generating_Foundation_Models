"""


"""

import re

def max_age(s):
    max_age = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j].isdigit():
                max_age = max(max_age, int(s[i:j]))
            else:
                for k in range(i, j):
                    if s[k].isalpha():
                        max_age = max(max_age, int(s[i:k]+s[k].lower()+s[k+1:j]))
    return max_age

s = "C0D3C43F"
print(max_age(s))