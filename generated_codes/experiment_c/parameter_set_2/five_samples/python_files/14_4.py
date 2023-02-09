'''

'''

# Write your code here

def count_operations(a, b):
    count = 0
    while a != b:
        if a > b:
            if a % 2 == 0:
                a = a // 2
            else:
                a = (a - 1) // 2
        else:
            a = a * 2
        count += 1
    return count

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(count_operations(a, b))