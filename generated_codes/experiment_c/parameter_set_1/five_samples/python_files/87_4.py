'''


Explanation

In the example test case, the third friend will be locked in the first house,
the second friend will be locked in the second house, and the first friend
will be locked in the third house.

"""
def is_possible(n, fre, house):
    if n==0:
        return True
    for i in range(n):
        if fre[i] == 0:
            for j in range(n):
                if house[i][j] == 0:
                    fre[i] = house[i][j] = 1
                    if is_possible(n, fre, house):
                        return True
                    fre[i] = house[i][j] = 0
    return False
    
    
    
    
def magic_land(n, house):
    fre = [0]*n 
    if is_possible(n, fre, house):
        print(" ".join(str(i) for i in fre))
    else:
        print(-1)
n = int(input())
house = [[int(j) for j in input().split()] for i in range(n)]
magic_land(n, house)

'''

def is_possible(n, fre, house):
    if n==0:
        return True
    for i in range(n):
        if fre[i] == 0:
            for j in range(n):
                if house[i][j] == 0:
                    fre[i] = house[i][j] = 1
                    if is_possible(n, fre, house):
                        return True
                    fre[i] = house[i][j] = 0
    return False
    
    
    
    
def magic_land(n, house):
    fre = [0]*n 
    if is_possible(n, fre, house):
        print(" ".join(str(i) for i in fre))
    else:
        print(-1)
n = int(input())
house = [[int(j) for j in input().split()] for i in range(n)]
magic_land(n, house)
'''