'''
 pairs.
Case 4 : N = 6. Arjuna can make the pair (1,4). Bhima can not make any more pairs ( without crossing the pair (1,4) )

'''

#code

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def is_odd(n):
    if n % 2 == 0:
        return False
    return True

def is_even(n):
    if n % 2 == 0:
        return True
    return False

def is_power_of_two(n):
    if n == 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True

def is_power_of_three(n):
    if n == 0:
        return False
    while n != 1:
        if n % 3 != 0:
            return False
        n = n // 3
    return True

def is_power_of_four(n):
    if n == 0:
        return False
    while n != 1:
        if n % 4 != 0:
            return False
        n = n // 4
    return True

def is_power_of_five(n):
    if n == 0:
        return False
    while n != 1:
        if n % 5 != 0:
            return False
        n = n // 5
    return True

def is_power_of_six(n):
    if n == 0:
        return False
    while n != 1:
        if n % 6 != 0:
            return False
        n = n // 6
    return True

def is_power_of_seven(n):
    if n == 0:
        return False
