"""

"""

def max_speed(n, speed):
    max_speed = speed[0]
    count = 0
    for i in range(n):
        if speed[i] <= max_speed:
            count += 1
            max_speed = speed[i]
    return count

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        speed = list(map(int, input().split()))
        print(max_speed(n, speed))