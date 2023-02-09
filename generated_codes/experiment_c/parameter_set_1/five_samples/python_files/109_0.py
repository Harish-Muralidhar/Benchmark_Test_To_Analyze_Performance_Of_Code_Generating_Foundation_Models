"""

"""

# Write your code here
def check_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def check_line(c):
    return (c/2).is_integer()

for _ in range(int(input())):
    side = int(input())
    if check_line(side) and check_triangle(side, side, side + 2):
        print("YES")
    else:
        print("NO")