"""

"""
import math

def check_mid(x1,x2,y):
    if x1 == 0 or x2 == 0:
        return 0
    if y == 0:
        return 0
    if x1 > 0 and x2 > 0:
        if y > 0:
            if x2 > y:
                if x1 < y:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            if x1 > abs(y):
                if x2 < abs(y):
                    return 1
                else:
                    return 0
            else:
                return 0
    elif x1 < 0 and x2 < 0:
        if y > 0:
            if abs(x1) > y:
                if abs(x2) < y:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            if abs(x2) > abs(y):
                if abs(x1) < abs(y):
                    return 1
                else:
                    return 0
            else:
                return 0
    else:
        return 0

def check(x1,x2,y):
    if x1 == 0 or x2 == 0:
        return 0
    if y == 0:
        return 0
    if x1 > 0 and x2 > 0:
        if y > 0:
            return 1
        else:
            return 0
    elif x1 < 0 and x2 < 0:
        if y > 0:
            return 0
        else:
            return 1
    else:
        return 0

def get_no_of_guns(x1,x2,y):
    #print x1,x2,y
    y = abs(y)
    hcf = math.gcd(math.gcd(x1,x2),y)
    #print hcf
    if hcf != 1:
        if hcf != x1 and hcf != x2 and hcf != y:
            return 0
    if abs(x1) == abs(x2):
        if x1*x2 >= 0:
            if x1*x2*y >= 0:
                return 0
            else:
                return 1
        else:
            return 0
    else:
        if x1 == y or x2 == y:
            return 1
        else:
            #print "check",check(x1,x2,y)
            #print "check_mid",check_mid(x1,x2,y)
            if x1*x2*y >= 0:
                return 1 + check(x1,x2,y)
            else:
                return max(check(x1,x2,y),check_mid(x1,x2,y))
    #return 0

t = int(raw_input())
for _ in range(t):
    x = [int(x) for x in raw_input().split()]
    x1 = x[1]
    x2 = x[2]
    y = x[0]
    print get_no_of_guns(x1,x2,y)