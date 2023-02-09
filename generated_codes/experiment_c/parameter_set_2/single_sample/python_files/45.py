"""

"""

import collections

def check_occurence(string):
    if len(string) == 0:
        return "NO"
    if len(string) == 1:
        return "YES"
    count = collections.Counter(string)
    if len(count) == 1:
        return "YES"
    if len(count) == 2:
        return "YES"
    if len(count) > 2:
        return "NO"

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        string = input()
        print(check_occurence(string))