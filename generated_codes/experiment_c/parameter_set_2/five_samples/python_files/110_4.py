"""

"""

# Write your code here

def split(s):
    if len(s) == 1:
        return [s, ""]
    else:
        return [s[:len(s)//2], s[len(s)//2:]]

def hash(s):
    result = s.count("A")
    if len(s) > 1:
        s1, s2 = split(s)
        result += max(hash(s1), hash(s2))
    return result

def count_strings(a, e, v):
    if a == 0:
        if e == 0 and v == 0:
            return 1
        else:
            return 0
    else:
        if v >= a:
            return count_strings(a-1, e, v-a) + count_strings(a, e-1, v)
        else:
            return count_strings(a-1, e, v)

t = int(input())
for i in range(t):
    a, e, v = map(int, input().split())
    print(count_strings(a, e, v))