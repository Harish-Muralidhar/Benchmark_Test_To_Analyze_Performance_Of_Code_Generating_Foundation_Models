"""

Input:
23764

Output:
0

Input:
454

Output:
1

Input:
42

Output:
1

Input:
4444444444444

Output:
13
)
"""

def find_fours(n):
    four_counter = 0
    for digit in str(n):
        if digit == '4':
            four_counter += 1
    return four_counter

num = int(input())
for i in range(num):
    print(find_fours(int(input())))