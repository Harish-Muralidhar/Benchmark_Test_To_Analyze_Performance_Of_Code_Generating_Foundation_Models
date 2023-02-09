"""



"""

t = int(input())
for i in range(t):
    k = int(input())
    s = input()
    l = len(s)
    if l == 1 and s == '?':
        print(0)
    elif l == 1 and s != '?':
        print(s)
    elif l > 1:
        if s[0] == '?' and s[1] == '?':
            print(0, end='')
            for j in range(1, l):
                if s[j] == '?':
                    print(1, end='')
                else:
                    print(s[j], end='')
            print()
        elif s[0] == '?' and s[1] != '?':
            print(int(s[1]) + 1, end='')
            for j in range(1, l):
                if s[j] == '?':
                    print(0, end='')
                else:
                    print(s[j], end='')
            print()
        elif s[0] != '?' and s[1] == '?':
            print(s[0], end='')
            for j in range(1, l):
                if s[j] == '?':
                    print(0, end='')
                else:
                    print(s[j], end='')
            print()
        elif s[0] != '?' and s[1] != '?':
            if s[0] == s[1]:
                print('NO')
            else:
                print(s[0], end='')
                for j in range(1, l):
                    if s[j] == '?':
                        print(0, end='')
                    else:
                        print(s[j], end='')
                print()