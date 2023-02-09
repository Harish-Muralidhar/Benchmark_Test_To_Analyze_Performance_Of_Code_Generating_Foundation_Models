'''
Subtasks

Subtask #1 (100 points): Original constraints
'''



import sys

def is_substring(s, d):
    n = len(s)
    m = len(d)
    for i in range(n-m+1):
        if s[i:i+m] == d:
            return True
    return False

def is_in_dict(s, d):
    for i in d:
        if is_substring(s, i):
            return True
    return False

def dp(s, d):
    if is_in_dict(s, d):
        return False
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            if not is_in_dict(s[i:j], d):
                return True
    return False

def solve():
    inp = sys.stdin.readlines()
    i = 0
    while i < len(inp):
        s = inp[i].strip()
        i += 1
        n = int(inp[i])
        i += 1
        d = []
        while n:
            d.append(inp[i].strip())
            i += 1
            n -= 1
        if dp(s, d):
            print("Teddy")
        else:
            print("Tracy")

if __name__ == "__main__":
    solve()