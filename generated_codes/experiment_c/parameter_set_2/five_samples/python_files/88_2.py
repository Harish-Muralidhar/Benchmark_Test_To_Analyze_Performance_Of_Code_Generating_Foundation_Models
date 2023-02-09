"""


"""

import math

def main():
    N, M, Q = map(int, input().split())
    Sx, Sy = map(int, input().split())
    P1 = []
    P2 = []
    for i in range(6):
        p1, p2 = map(int, input().split())
        P1.append(p1)
        P2.append(p2)
    T = []
    for i in range(Q):
        t = int(input())
        T.append(t)
    for t in T:
        print(calculate_images(N, M, Sx, Sy, P1, P2, t))

def calculate_images(N, M, Sx, Sy, P1, P2, T):
    images = 1
    for i in range(1, T + 1):
        images += calculate_images_for_move(N, M, Sx, Sy, P1, P2, i)
    return images

def calculate_images_for_move(N, M, Sx, Sy, P1, P2, T):
    images = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            images += calculate_images_for_cell(N, M, Sx, Sy, P1, P2, T, i, j)
    return images

def calculate_images_for_cell(N, M, Sx, Sy, P1, P2, T, i, j):
    images = 0
    if i == Sx and j == Sy:
        images += 1
    if T == 1:
        return images
    F = calculate_F(N, M, i, j)
    X = F % 6
    D1, D2, P1_, P2_ = get_D1_D2_P1_P2(X, P1, P2)
    images += calculate_images_for_cell_in_direction(N, M, i, j, D1, P1_, T)
    images += calculate_