'''

'''

#code

def find_collision(arr, n, m):
    collision = 0
    for i in range(m):
        count = 0
        for j in range(n):
            if arr[j][i] == 1:
                count += 1
        collision += count * (count - 1) // 2
    return collision

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input())))
    print(find_collision(arr, n, m))