'''


'''

t = int(input())
for i in range(t):
    n, origin = input().split()
    n = int(n)
    laddus = 0
    for i in range(n):
        s = input().split()
        if s[0] == 'CONTEST_WON':
            laddus += 300
            if int(s[1]) < 20:
                laddus += 20 - int(s[1])
        elif s[0] == 'TOP_CONTRIBUTOR':
            laddus += 300
        elif s[0] == 'BUG_FOUND':
            laddus += int(s[1])
        elif s[0] == 'CONTEST_HOSTED':
            laddus += 50
    if origin == 'INDIAN':
        print(laddus // 200)
    else:
        print(laddus // 400)