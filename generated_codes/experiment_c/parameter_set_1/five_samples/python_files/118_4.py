'''

'''

import sys
import copy

def get_max(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    max_val = lst[0]
    max_idx = 0
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            max_idx = i
    return max_idx

def get_min(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    min_val = lst[0]
    min_idx = 0
    for i in range(1, len(lst)):
        if lst[i] < min_val:
            min_val = lst[i]
            min_idx = i
    return min_idx

def get_max_idx(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return 0
    max_val = lst[0]
    max_idx = 0
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            max_idx = i
    return max_idx

def get_min_idx(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return 0
    min_val = lst[0]
    min_idx = 0
    for i in range(1, len(lst)):
        if lst[i] < min_val:
            min_val = lst[i]
            min_idx = i
    return min_idx

def get_max_2(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    max_val = lst[0]
    max_idx = 0
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            max_idx = i
    return max_idx, max_val

def get_min_2(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    min_val = lst[0]
    min_idx = 0
    for i in range(1, len(lst)):
        if lst[i] < min_val:
            min_val = lst[i]
            min_idx = i
    return min_idx, min_val

def left_rotate(lst, n):
    return lst[n:] + lst[:n]

def get_pairs(lst, n):
    lst = copy.deepcopy(lst)
    lst = sorted(lst)
    print(lst, n)
    ans = 0
    for i in range(n//2):
        ans += lst[i]
    return ans

def find_min_cost(lst, n):
    lst = copy.deepcopy(lst)
    ans = 0
    while len(lst) > 1:
        max_idx = get_max_idx(lst)
        min_idx = get_min_idx(lst)
        print(lst, max_idx, min_idx)
        if max_idx > min_idx:
            min_idx_2 = get_min_idx(lst[min_idx+1:]) + min_idx + 1
        else:
            min_idx_2 = get_min_idx(lst[:min_idx])
        lst = left_rotate(lst, min_idx_2)
        print(lst, min_idx_2)
        max_idx, max_val = get_max_2(lst)
        min_idx, min_val = get_min_2(lst)
        lst = lst[2:]
        ans += min_val + min_val
    return ans

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        ans = find_min_cost(lst, n)
        print(ans)

if __name__ == "__main__":
    main()