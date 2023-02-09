"""


"""

# Write your code here
import re

def check(s):
    if(s.isdigit()):
        return True
    else:
        return False

def max_age(s):
    s = s.upper()
    max_age = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if(check(s[i:j])):
                if(int(s[i:j])>max_age):
                    max_age = int(s[i:j])
    return max_age

def max_age1(s):
    s = s.upper()
    max_age = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if(check(s[i:j])):
                if(int(s[i:j])>max_age):
                    max_age = int(s[i:j])
            else:
                for k in range(i,j):
                    if(s[k].isalpha()):
                        if(check(s[i:k]+s[k+1:j])):
                            if(int(s[i:k]+s[k+1:j])>max_age):
                                max_age = int(s[i:k]+s[k+1:j])
    return max_age

s = input()
print(max_age1(s))