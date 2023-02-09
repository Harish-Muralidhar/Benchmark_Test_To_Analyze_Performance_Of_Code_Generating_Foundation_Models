'''

'''

# Write your code here

def split(s):
    l = len(s)
    if l == 1:
        return (s, '')
    else:
        return (s[0:l//2], s[l//2:])

def hash(s):
    result = s.count('A')
    if len(s) > 1:
        (s1, s2) = split(s)
        result = result + max(hash(s1), hash(s2))
    return result

def solve(a, e, v):
    if a > v or e > v:
        return 0
    if a == v or e == v:
        return 1
    if a == 0:
        return 1
    if e == 0:
        return 1
    return (solve(a-1, e, v-1) + solve(a, e-1, v-1)) % 1000000007

t = int(input())
for _ in range(t):
    a, e, v = map(int, input().split())
    print(solve(a, e, v))