"""



Sample Explanation

In the sample case, the best solution is to remove the barricades at (2,2) and (2,1) for a total cost of 1+1=2.
"""
import math

def solve(w, h, d, n, barricades):
    corner_barracades = []
    barrancade_at_center = ()
    barrancade_along_diagonal = ()
    barrancade_at_edge = []
    
    for barricade in barricades:
        if barricade[0] == 0 or barricade[0] == w-2*d or barricade[1] == 0 or barricade[1] == h-2*d:
            corner_barracades.append((barricade[0], barricade[1], barricade[2]))
        elif barricade[0] == w/2-d and barricade[1] == h/2-d:
            barrancade_at_center = (barricade[0], barricade[1], barricade[2])
        elif barricade[0] == d and barricade[1] == h/2-d or barricade[0] == w/2-d and barricade[1] == d or barricade[0] == w - d and barricade[1] == h/2-d or barricade[0] == w/2-d and barricade[1] == h - d:
            barrancade_along_diagonal = (barricade[0], barricade[1], barricade[2])
        else:
            barrancade_at_edge.append((barricade[0], barricade[1], barricade[2]))
    
    cost = 0
    if barrancade_at_center:
        cost += barrancade_at_center[2]
    
    if barrancade_along_diagonal:
        cost += barrancade_along_diagonal[2]
    
    for barricade in barrancade_at_edge:
        if barricade[0] == w/2-d or barricade[1] == h/2-d:
            cost += barricade[2]
    
    for barricade in corner_barracades:
        if barricade[0] == w/2-d or barricade[1] == h/2-d:
            cost += barricade[2]
        elif barricade[0] == w/2 - d or barricade[1] == h/2 - d:
            cost += barricade[2]
        elif barricade[0] == 0 and barricade[1] == 0:
            cost += barricade[2]
        elif barricade[0] == 0 and barricade[1] == h - 2*d:
            cost += barricade[2]
        else:
            cost += barricade[2]
    
    return cost

if __name__ == "__main__":
    w, h, d, n = [int(x) for x in input().split()]
    barricades = []
    for i in range(n):
        barricades.append([int(x) for x in input().split()])
    print(solve(w, h, d, n, barricades))