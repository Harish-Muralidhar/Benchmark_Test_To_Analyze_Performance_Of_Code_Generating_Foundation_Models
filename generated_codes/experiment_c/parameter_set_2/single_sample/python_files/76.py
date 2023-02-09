"""
"""

def get_min_people(X, dishes, clans):
    # Write your code here
    pass


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        X = int(input())
        B = int(input())
        dishes = []
        for _ in range(B):
            dishes.append(list(map(int, input().split())))
        C = int(input())
        clans = []
        for _ in range(C):
            clans.append(list(map(int, input().split())))
        print(get_min_people(X, dishes, clans))