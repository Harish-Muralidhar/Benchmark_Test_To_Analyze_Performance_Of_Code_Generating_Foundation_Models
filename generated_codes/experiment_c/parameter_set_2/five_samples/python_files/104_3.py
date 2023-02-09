"""

"""

import random

def generate_string(n):
    s = ""
    for i in range(n):
        s += random.choice(["A", "B"])
    return s

def find_subsequence(s):
    for i in range(1, len(s)):
        t = s[:i]
        if s.count(t) == 2:
            return t
    return -1

def main():
    t = int(input())
    for i in range(t):
        n = random.randint(1, 100)
        s = generate_string(n)
        print(s)
        print(find_subsequence(s))

if __name__ == "__main__":
    main()