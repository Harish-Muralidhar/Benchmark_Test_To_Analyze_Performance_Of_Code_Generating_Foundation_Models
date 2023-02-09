"""

"""

def check_substring(s,d):
    for i in range(len(s)):
        if s[i:len(d)+i] == d:
            return True
    return False

def check_winner(s,d):
    if len(s) == 0:
        return "Tracy"
    for i in range(len(d)):
        if check_substring(s,d[i]):
            return check_winner(s.replace(d[i],""),d)
    return "Teddy"

t = int(input())
for i in range(t):
    s = input()
    n = int(input())
    d = []
    for j in range(n):
        d.append(input())
    print(check_winner(s,d))