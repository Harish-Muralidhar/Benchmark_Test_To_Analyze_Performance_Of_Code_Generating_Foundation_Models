"""


"""

# Write your code here

n = int(input())

a = list(map(int, input().split()))

count = 0

for i in a:
    if i % 2 == 0:
        count += 1

if count > (n - count):
    print("READY FOR BATTLE")
else:
    print("NOT READY")