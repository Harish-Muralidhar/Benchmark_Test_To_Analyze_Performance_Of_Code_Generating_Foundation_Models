"""

"""

# Write your code here

test = int(input())

for i in range(test):
    angles = list(map(int, input().split()))
    if sum(angles) == 180:
        print("YES")
    else:
        print("NO")