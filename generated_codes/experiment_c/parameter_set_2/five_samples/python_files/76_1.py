'''

'''


def min_chefs(x, b, c):
    dishes = list()
    clans = list()
    for i in range(b):
        dishes.append(list(map(int, input().split())))
    for i in range(c):
        clans.append(list(map(int, input().split())))
    dishes.sort()
    clans.sort()
    print(dishes)
    print(clans)
    return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        x = int(input())
        b = int(input())
        c = int(input())
        print(min_chefs(x, b, c))