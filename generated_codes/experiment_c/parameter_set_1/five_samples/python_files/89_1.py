'''

'''

n,m = map(int,input().split())
defence = []
number = 0

for i in range(m):
    l = list(input().split())
    if l[0] == 'P':
        defence.append([int(l[1]),int(l[2])])
        number += 1
    elif l[0] == 'M':
        defence[int(l[1])-1] = [defence[int(l[1])-1][0]+int(l[2]),defence[int(l[1])-1][1]+int(l[2])]
    else:
        count = 0
        for i in defence:
            if i[0] <= int(l[1]) <= i[1]:
                count +=1
        print(count)