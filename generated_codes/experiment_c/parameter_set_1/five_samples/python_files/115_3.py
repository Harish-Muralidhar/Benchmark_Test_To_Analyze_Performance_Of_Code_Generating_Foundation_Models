"""

"""


def chef_and_game(data):
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            if data[i] > data[j]:
                data[i] = data[i] - data[j]

    return data[0]


if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        size = input()
        arr = [int(i) for i in input().split()][0:int(size)]
        print(chef_and_game(arr))