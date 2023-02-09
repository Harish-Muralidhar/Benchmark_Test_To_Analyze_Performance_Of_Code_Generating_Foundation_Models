"""

"""

# cook your dish here
for _ in range(int(input())):
    x = int(input())
    b = int(input())
    dishes = list(map(int,input().split()))
    c = int(input())
    clans = list(map(int,input().split()))
    if c == 0:
        if dishes[0] == 1:
            print(2)
        else:
            print(dishes[0])
    else:
        if dishes[0] == 1:
            print(2)
        else:
            print(dishes[0])