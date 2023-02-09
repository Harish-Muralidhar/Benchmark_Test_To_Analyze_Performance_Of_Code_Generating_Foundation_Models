'''


SOLUTION:
'''

import re
def is_valid(n):
    if n>=0 and n<=9:
        return True
    return False
def get_number(s):
    n=0
    for i in range(len(s)):
        if s[i]>='0' and s[i]<='9':
            n=n*10+(ord(s[i])-48)
        else:
            break
    return n
def is_valid_for_substring(s,n):
    if len(s)<=len(str(n)):
        return False
    if s[:len(str(n))]==str(n):
        return True
    return False

def solve(s):
    l=get_number(s)
    for i in range(len(s)):
        if s[i]>='A' and s[i]<='Z':
            for j in range(10):
                if is_valid_for_substring(s,l-j):
                    return l-j
            for j in range(10):
                if is_valid_for_substring(s,l+j):
                    return l+j
    return l
t=int(input())
for i in range(t):
    n=input()
    print(solve(n))