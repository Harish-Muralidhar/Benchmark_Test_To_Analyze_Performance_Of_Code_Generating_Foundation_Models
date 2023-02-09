"""


"""

# Write your code here

def find_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 5
    if n == 3:
        return 11
    return find_ways(n-1) + find_ways(n-2) + find_ways(n-3)

t = int(input())
for i in range(t):
    n = int(input())
    print(find_ways(n) % 1000000007)