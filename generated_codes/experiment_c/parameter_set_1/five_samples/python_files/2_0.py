'''


'''

n = int(input())
weapons = list(map(int,input().split()))
count = 0
for i in range(len(weapons)):
    if weapons[i] % 2 == 0:
        count = count + 1
    else:
        count = count
if count > n - count:
    print("READY FOR BATTLE")
else:
    print("NOT READY")