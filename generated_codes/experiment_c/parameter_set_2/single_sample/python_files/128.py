'''

'''

import sys

def get_smallest_lexicographical_subsequence(s, k):
    if k == 0:
        return ""
    if k == len(s):
        return s
    min_char = min(s)
    min_char_index = s.index(min_char)
    return min_char + get_smallest_lexicographical_subsequence(s[min_char_index+1:], k-1)

def main():
    test_cases = int(input())
    for i in range(test_cases):
        s = input()
        k = int(input())
        print(get_smallest_lexicographical_subsequence(s, k))

if __name__ == '__main__':
    main()