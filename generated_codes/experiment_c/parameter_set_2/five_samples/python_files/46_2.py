'''


'''

def collision(arr, n, m):
    count = 0
    for i in range(m):
        for j in range(i+1, m):
            for k in range(n):
                if arr[k][i] == 1 and arr[k][j] == 1:
                    count += 1
    return count

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = []
    for j in range(n):
        arr.append(list(map(int, input())))
    print(collision(arr, n, m))