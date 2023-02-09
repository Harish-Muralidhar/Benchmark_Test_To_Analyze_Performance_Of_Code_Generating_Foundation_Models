'''


'''

# Solution

for i in range(int(input())):
    n = int(input())
    s = input()
    r = g = b = 0
    for i in s:
        if i == 'R':
            r += 1
        elif i == 'G':
            g += 1
        else:
            b += 1
    print(n - max(r, g, b))