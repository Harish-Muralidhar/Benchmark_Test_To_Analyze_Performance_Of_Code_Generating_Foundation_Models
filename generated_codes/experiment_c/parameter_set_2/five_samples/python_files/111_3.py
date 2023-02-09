'''


'''

import re

def max_age(s):
    max_age = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[i] in '0123456789':
                if s[j] in '0123456789':
                    age = s[i:j+1]
                    if int(age) > max_age:
                        max_age = int(age)
            else:
                if s[j] in '0123456789':
                    age = s[i:j+1]
                    if int(age) > max_age:
                        max_age = int(age)
                else:
                    age = s[i:j+1]
                    if int(re.sub('[A-Z]','9',age)) > max_age:
                        max_age = int(re.sub('[A-Z]','9',age))
    return max_age

if __name__ == '__main__':
    s = raw_input()
    print max_age(s)