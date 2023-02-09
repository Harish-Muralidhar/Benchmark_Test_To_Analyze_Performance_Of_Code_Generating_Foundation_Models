"""

In the third example,
You will need to paint 2 balloons to make all of the same color.
"""

for _ in range(int(input())):
    s = input()
    cnt1 = cnt2 = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'b':
                cnt1 += 1
            else:
                cnt2 += 1
        else:
            if s[i] == 'b':
                cnt2 += 1
            else:
                cnt1 += 1
    print(min(cnt1, cnt2))