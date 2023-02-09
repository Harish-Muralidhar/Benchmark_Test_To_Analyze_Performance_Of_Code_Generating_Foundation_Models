'''

Explanation
Example case 1: Joe can play the beats (2, 5, 8, 11) while Chef can play the beats (4, 8, 16).
Example case 2: Joe can play the beats (2, 3, 4, 5) while Chef can play the beats (1, 2, 4).
Example case 3: Joe can play the beats (2, 3, 9, 10, 19, 27, 28) while Chef can play the beats (1, 3, 9, 27, 81).
Example case 4: Joe can play the beats (4, 7, 10, 13, 25) while Chef can play the beats (1, 4, 7, 10, 25).

'''

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

def get_arithmetic_progression(a, b, n):
    d = (b - a) / (n - 1)
    return [a + d * i for i in range(n)]

def get_geometric_progression(a, b, n):
    r = b / a
    return [a * r ** i for i in range(n)]

def get_arigeom_progression(a, b, n):
    d = (b - a) / (n - 1)
    r = b / a
    return sorted(set(get_arithmetic_progression(a, b, n) + get_geometric_progression(a, b, n)))

def get_arigeom_progression_from_list(l):
    n = len(l)
    if n == 2:
        return l
    a = l[0]
    b = l[-1]
    return get_arigeom_progression(a, b, n)

def get_arigeom_progression_from_list_with_common_ratio(l):
    n = len(l)
    if n == 2:
        return l
    a = l[0]
   