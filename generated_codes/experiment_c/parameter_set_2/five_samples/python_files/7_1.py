"""

In the third example,
you can paint the first and last balloon. So, the answer is 2.

"""

# Write your code here

t = int(input())

for i in range(t):
    s = input()
    if s.count('a') == s.count('b'):
        print(0)
    else:
        print(abs(s.count('a') - s.count('b')))