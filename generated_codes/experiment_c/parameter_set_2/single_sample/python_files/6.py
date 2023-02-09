'''

'''

for i in range(int(input())):
    s1 = input()
    s2 = input()
    count = 0
    for i in range(len(s1)):
        if s1[i] == '?' or s2[i] == '?':
            count += 1
        elif s1[i] != s2[i]:
            count += 1
    print(count, count + len(s1) - count)