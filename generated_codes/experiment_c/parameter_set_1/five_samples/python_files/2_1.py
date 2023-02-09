'''


'''

n = int(input())
arr = list(map(int, input().split()))

count = 0
for i in arr:
    if i % 2 == 0:
        count += 1

if count > n - count:
    print('READY FOR BATTLE')
else:
    print('NOT READY')