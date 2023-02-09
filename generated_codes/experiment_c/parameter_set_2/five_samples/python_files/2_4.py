'''


'''

# Write your code here
import sys
n = int(input())
a = list(map(int,input().split()))
count_even = 0
count_odd = 0
for i in a:
    if i%2 == 0:
        count_even += 1
    else:
        count_odd += 1
if count_even > count_odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")