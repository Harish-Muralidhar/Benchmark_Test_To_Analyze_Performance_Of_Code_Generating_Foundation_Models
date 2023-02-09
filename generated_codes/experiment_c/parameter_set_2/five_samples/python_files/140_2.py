"""


"""

# Write your code here

def building_wall(n):
    if n == 1:
        return 1
    elif n == 2:
        return 5
    elif n == 3:
        return 11
    else:
        return building_wall(n-1) + 5*building_wall(n-2) + building_wall(n-3) - building_wall(n-4)

t = int(input())
for i in range(t):
    n = int(input())
    print(building_wall(n)%1000000007)