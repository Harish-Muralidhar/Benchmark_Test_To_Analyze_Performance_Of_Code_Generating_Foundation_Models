'''

'''

# Write your code here

def min_rooms(n, s):
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    if r == n or g == n or b == n:
        return 0
    else:
        return min(r, g, b)

T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    print(min_rooms(n, s))