'''


'''

#Solution

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

def count_substrings(s):
    n = len(s)
    c = Counter(s)
    return (c['A']*c['B']*c['C']) + (n*(n-1)*(n-2))//6
    
s = input()
print(count_substrings(s))