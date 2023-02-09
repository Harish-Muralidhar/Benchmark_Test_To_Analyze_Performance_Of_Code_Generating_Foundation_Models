/*
ai <= bi

*/
n = int(input().strip())
for t in range(n):
    n1 = raw_input()
    pairs = []
    knight = 0
    knave = 0
    is_knight = []
    for i in range(int(n1)):
        a, b = map(int, raw_input().strip().split())
        if a == 0 and b == 0:
            knight += 1
            is_knight.append(1)
        elif a == (b+1):
            knave += 1
            is_knight.append(0)
        else:
            pairs.append((a,b))
    pairs.sort(key = lambda x: x[1] - x[0], reverse = True)
    for i in range(len(pairs)):
        if pairs[i][0] == 1 and pairs[i][1] == 1:
            knight += 1
            is_knight.append(1)
            pairs[i] = None
        elif pairs[i][0] == 0 and pairs[i][1] == 1:
            knave += 1
            is_knight.append(0)
            pairs[i] = None
    i = 0
    pairs = [x for x in pairs if x != None]
    while i < len(pairs):
        a = pairs[i][0]
        b = pairs[i][1]
        if (a == 0 and b == 0) or (a == (b+1)):
            i = i + 1
            continue
        for j in range(i+1, len(pairs)):
            if pairs[j][0] >= a and pairs[j][1] <= b:
                a = pairs[j][0]
                b = pairs[j][1]
                pairs[j] = None
            elif pairs[j][0] > a and pairs[j][1] > b:
                pairs[j] = None
        pairs = [x for x in pairs if x != None]
        knight += 1
        is_knight.append(1)
        i = 0
    if knight + knave == int(n1):
        print knight
        for x in is_knight:
            print x,
    else:
        print "0"