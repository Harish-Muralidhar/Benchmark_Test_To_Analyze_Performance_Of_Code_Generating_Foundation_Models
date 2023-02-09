"""

Explanation
In the first case, the character 'a' occurs once, the character 'c' occurs once and the character 'b' occurs once. So the answer is YES.
In the second case, the character 'z' occurs 3 times, the character 'q' occurs 3 times and the character 'w' occurs once. So the answer is YES.
In the third case, the character 'a' occurs once, the character 'b' occurs once and the character 'c' occurs once. But the character 'a' does not occur 3 times. So the answer is NO.
In the fourth case, the character 'k' occurs 2 times, the character 'l' occurs once, the character 'w' occurs 4 times. So the answer is YES.
"""

#code
for _ in range(int(input())):
    s = input()
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    if len(d) == 1:
        print("YES")
    else:
        l = list(d.values())
        if l.count(l[0]) == len(l):
            print("YES")
        else:
            print("NO")