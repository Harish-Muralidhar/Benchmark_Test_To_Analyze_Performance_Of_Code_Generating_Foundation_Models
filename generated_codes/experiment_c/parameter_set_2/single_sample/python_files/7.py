'''

In the third example,
you can paint the first and last balloon. So, the answer is 2.

'''

def min_flips(s):
    count = 0
    for i in range(len(s)):
        if s[i] != s[-1]:
            count += 1
    return count

t = int(input())
for i in range(t):
    s = input()
    print(min_flips(s))