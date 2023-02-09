'''

'''

# your code goes here
t = int(input())
for _ in range(t):
    n = int(input())
    a = 0
    b = 1
    while b < n:
        a, b = b, a + b
    if b == n:
        print('YES')
    else:
        print('NO')