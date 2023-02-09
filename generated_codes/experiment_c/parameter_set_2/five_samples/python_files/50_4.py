'''


'''

from collections import Counter

def count_substrings(s):
    c = Counter(s)
    return c['A']*c['B']*c['C']

if __name__ == '__main__':
    s = input()
    print(count_substrings(s))