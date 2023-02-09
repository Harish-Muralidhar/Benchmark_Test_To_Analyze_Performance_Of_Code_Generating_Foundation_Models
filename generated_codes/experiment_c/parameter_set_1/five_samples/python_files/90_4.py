"""
The provided office cannot be built.

"""


import sys

stdin = sys.stdin


def readline():
    return stdin.readline().strip()


def readint():
    return int(readline())


def readints():
    return (int(x) for x in readline().split())


def readinttab(n):
    return [int(x) for x in readline().split()]


def main(w, h, d, n, X, Y, C):
    """
    Dans le cas où je peux voir deux murs de l'autre côté de mon carré, il faut absolument qu'il n'y en ait pas entre les deux
    :param w: largeur
    :param h: hauteur
    :param d: rayon de la future maison
    :param n: nombre de murs
    :param X: abscisses des murs
    :param Y: ordonnées des murs
    :param C: coût des murs
    :return:
    """
    # on fabrique un tableau "murs" qui contient les murs horizontaux et verticaux
    # on peut le faire en O(n)
    murs = [[] for _ in range(2 * h + 2 * w)]  # O(w+h)
    for x, y, c in zip(X, Y, C):
        murs[x - 1].append([c, y - 1])
        murs[y + h].append([c, x - 1])
    for lm in murs:
        lm.sort()
    # ok, maintenant, on va parcourir tous les murs en O(w+h)
    # à chaque fois, j'ai besoin de la liste des murs sur ma ligne, et ceux sur ma colonne
    # carré de centre (cx,cy) et de côtés 2d
    # le minimum est le minimum sur les 4 coordonnées, car il n'y a peut-être pas de murs sur l'une des 4 coordonnées
    # il faut aussi voir les murs qui sont entre les deux murs "visibles" dans les 2 autres directions
    # il faut voir les murs qui sont entre (cx - d + 1, cy - d + 1) et (cx + d, cy + d)
    # trouver le minimum sur cette zone
    min_cost = float("inf")
    for cx in range(0, w):
        for cy in range(0, h):
            lx = murs[cx + h]
            ly = murs[cy + w]
            # on va chercher les murs horizontaux et verticaux qui sont dans la zone
            # et on les trie
            murs_in_zone = sorted([c for c, x in lx if x >= cy - d + 1 and x <= cy + d]) + sorted([c for c, y in ly if y >= cx - d + 1 and y <= cx + d])
            # on peut les ajouter en O(n)
            if len(murs_in_zone) == 0:
                min_cost = 0
                continue
            # on prend le minimum
            min_cost = min(min_cost, sum(murs_in_zone))
    print(min_cost)


main(*readinttab(4), *zip(*[readinttab(3) for _ in range(readint())]))