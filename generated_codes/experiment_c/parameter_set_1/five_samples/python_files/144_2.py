'''

SOLUTION:
'''

def all_prime(num, list):
    for i in list:
        if num % i == 0:
            return False
    return True

t = int(input("Enter the number of testcases: "))

primes = []
for i in range(2, 50):
    if all_prime(i, primes):
        primes.append(i)

for _ in range(t):
    row, col = map(int, input("Enter the number of rows and columns: ").split())
    arr = []
    for i in range(row):
        arr.append(list(input()))

    cnt = 0
    for i in range(row):
        for j in range(col):
            if arr[i][j] == '#':
                continue
            else:
                left = 0
                right = 0
                top = 0
                bottom = 0
                for k in range(j, -1, -1):
                    if arr[i][k] == '#':
                        break
                    else:
                        left += 1
                for k in range(j, col):
                    if arr[i][k] == '#':
                        break
                    else:
                        right += 1
                for k in range(i, -1, -1):
                    if arr[k][j] == '#':
                        break
                    else:
                        top += 1
                for k in range(i, row):
                    if arr[k][j] == '#':
                        break
                    else:
                        bottom += 1
                mini = min(left, right, top, bottom)
                if mini in primes:
                    cnt += 1
    print(cnt)