"""

"""
for _ in range(int(input())):
    n, u, v = map(int, input().split())
    um, vm = max(u, v), min(u, v)
    ud, vd = (um - 1) // 2, (vm - 1) // 2
    if ud == vd:
        print(1)
    elif ud > vd:
        print((2 ** (ud - vd + 1)) - 1)
    else:
        t = 1
        while (vd & t) == 0:
            t <<= 1
        print(2 ** (vd - t + 1) - 1)