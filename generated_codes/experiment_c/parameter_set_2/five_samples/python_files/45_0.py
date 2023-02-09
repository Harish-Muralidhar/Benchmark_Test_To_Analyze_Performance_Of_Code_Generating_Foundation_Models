"""

Explanation
Case 1: a occurs 2 times and b occurs 1 time. 2 = 1 + 1.
Case 2: z occurs 4 times, q occurs 2 times and 2 = 4 + 0.
Case 3: a occurs 1 time, b occurs 1 time and c occurs 1 time. 1 != 1 + 1.
Case 4: k occurs 2 times, l occurs 1 time, w occurs 4 times and 2 = 1 + 1.

"""

#code

def is_equal(s):
    count = [0]*26
    for i in range(len(s)):
        count[ord(s[i])-ord('a')] += 1
    sum = 0
    for i in range(26):
        if count[i] == 0:
            continue
        if count[i] == sum:
            return True
        sum += count[i]
    return False

t = int(input())
while t > 0:
    s = input()
    if is_equal(s):
        print("YES")
    else:
        print("NO")
    t -= 1