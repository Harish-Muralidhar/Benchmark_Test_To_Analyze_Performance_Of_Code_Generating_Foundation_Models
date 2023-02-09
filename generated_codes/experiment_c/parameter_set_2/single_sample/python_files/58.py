'''


'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_bit(n, i):
    return (n & (1 << i)) != 0

def set_bit(n, i):
    return n | (1 << i)

def clear_bit(n, i):
    mask = ~(1 << i)
    return n & mask

def update_bit(n, i, v):
    if v == 0:
        return clear_bit(n, i)
    else:
        return set_bit(n, i)

def get_bit_count(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count

def get_bit_count_fast(n):
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
    return count

def get_bit_count_fast_2(n):
    count = 0
    while n > 0:
        count += 1
        n >>= 1
    return count

def get_bit_count_fast_3(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n >>= 1
    return count

def get_bit_count_fast_4(n):
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count

def get_bit_count_fast_5(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n >>= 1
    return count

def get_bit_count_fast_6(n):
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count

def get_bit_count_fast_7(n):
    count