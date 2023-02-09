'''

'''

T = int(input())
list = []

for i in range(T):
    N = int(input())
    if N < 10:
        list.append("What an obedient servant you are!")
    else:
        list.append("-1")

for i in range(T):
    print(list[i])