'''

https://www.codechef.com/problems/CHEFHASH
'''

def get_hash_val(A, E, V):
    hash_val = A
    if 1 < A + E:
        (S1, S2) = split(A, E)
        hash_val += max(get_hash_val(S1, S2, V - hash_val), get_hash_val(S2, S1, V - hash_val))
    return hash_val

def split(A, E):
    S1 = S2 = 0
    if 0 == A:
        S1 = 0
        S2 = E
    elif 0 == E:
        S1 = A
        S2 = 0
    else:
        if A < E:
            S1 = A
            S2 = E - A
        else:
            S1 = E
            S2 = A - E
    return S1, S2

def get_src_str_count(A, E, V):
    res = []
    def get_src_str_count_helper(A, E, V):
        if 0 == A + E and V == 0:
            res.append(1)
            return
        if 0 == V:
            return
        if 0 == A + E:
            return
        (S1, S2) = split(A, E)
        get_src_str_count_helper(S1, S2, V - 1)
        get_src_str_count_helper(S2, S1, V - 1)
    get_src_str_count_helper(A, E, V)
    return len(res)

def main():
    print(get_src_str_count(0, 0, 0))
    print(get_src_str_count(1, 0, 1))
    print(get_src_str_count(3, 2, 6))
    print(get_src_str_count(4, 2, 8))


if __name__ == '__main__':
    main()