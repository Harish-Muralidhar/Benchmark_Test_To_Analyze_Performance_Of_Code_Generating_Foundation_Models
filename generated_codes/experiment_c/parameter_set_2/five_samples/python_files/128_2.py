'''

'''

import sys

def get_smallest_lex_subseq(s, k):
    if len(s) < k:
        return -1
    if len(s) == k:
        return s
    else:
        return s[0] + get_smallest_lex_subseq(s[1:], k-1)

def main():
    t = int(input())
    for i in range(t):
        s = input()
        k = int(input())
        print(get_smallest_lex_subseq(s, k))

if __name__ == '__main__':
    main()