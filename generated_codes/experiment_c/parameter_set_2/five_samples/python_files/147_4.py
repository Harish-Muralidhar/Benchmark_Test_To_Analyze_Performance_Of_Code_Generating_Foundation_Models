"""

"""

def max_speed(n, speed):
    speed = sorted(speed)
    count = 0
    for i in range(n):
        if speed[i] == i+1:
            count += 1
    return count

t = int(input())
for i in range(t):
    n = int(input())
    speed = list(map(int, input().split()))
    print(max_speed(n, speed))