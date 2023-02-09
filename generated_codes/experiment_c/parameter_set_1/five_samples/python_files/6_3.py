'''

'''
for t in range(int(input())):
    S1 = input()
    S2 = input()
    count = 0
    for i in range(len(S1)):
        if S1[i] == '?' or S2[i] == '?':
            count += 1
        elif S1[i] != S2[i]:
            count += 1
    print(count, len(S1)-count)