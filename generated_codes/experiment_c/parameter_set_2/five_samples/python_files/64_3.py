'''
In the third case they are (2,0,0,0,0) and (1,1,0,0,0).

'''

import math
import itertools

def get_all_combinations(n, k):
    '''
    Returns all possible combinations of k elements from n elements
    '''
    return list(itertools.combinations(range(n), k))

def get_all_permutations(n, k):
    '''
    Returns all possible permutations of k elements from n elements
    '''
    return list(itertools.permutations(range(n), k))

def get_all_subsets(n, k):
    '''
    Returns all possible subsets of k elements from n elements
    '''
    return list(itertools.combinations(range(n), k))

def get_all_subsets_with_replacement(n, k):
    '''
    Returns all possible subsets of k elements from n elements
    '''
    return list(itertools.combinations_with_replacement(range(n), k))

def get_all_k_length_binary_strings(n, k):
    '''
    Returns all possible k length binary strings from n elements
    '''
    return list(itertools.product(range(n), repeat=k))

def get_all_k_length_binary_strings_with_sum_n(n, k):
    '''
    Returns all possible k length binary strings from n elements
    '''
    return list(itertools.product(range(n), repeat=k))

def get_all_k_length_binary_strings_with_sum_n_and_tuple(n, k):
    '''
    Returns all possible k length binary strings from n elements
    '''
    return list(itertools.product(range(n), repeat=k))

def get_all_k_length_binary_strings_with_sum_n_and_tuple_with_replacement(n, k):
    '''
    Returns all possible k