"""

https://www.codechef.com/problems/FLOW018
"""

def max_speed_cars(speeds):
    max_speed = max(speeds)
    return len([speed for speed in speeds if max_speed == speed])

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        num_cars = int(input())
        speeds = [int(x) for x in input().split()]
        print(max_speed_cars(speeds))