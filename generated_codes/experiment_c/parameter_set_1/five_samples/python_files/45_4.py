'''

'''

#code
for _ in range(int(input())):
    s = input()
    occur = set()
    sums = 0
    for i in s:
        occur.add(i)
        sums += ord(i)
    res = list(occur)
    res.sort()
    ans = 0
    for i in res:
        ans += ord(i)
    if ans == sums:
        print('YES')
    else:
        print('NO')