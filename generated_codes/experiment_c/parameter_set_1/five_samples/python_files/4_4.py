'''

Test 1:
Input:
3
3
1 3 2
Output:
4
Expected:
4

Test 2:
Input:
4
4
4 1 2 1
Output:
5
Expected:
5

Test 3:
Input:
6
1 2 2 2 2 1
Output:
9
Expected:
9

Test 4:
Input:
1
1
1
Output:
1
Expected:
1

Test 5:
Input:
6
1 2 3 4 5 6
Output:
6
Expected:
6

Test 6:
Input:
6
1 2 3 4 5 6
Output:
6
Expected:
6

Test 7:
Input:
5
1 1 1 1 1
Output:
15
Expected:
15

Test 8:
Input:
5
1 1 1 1 1
Output:
15
Expected:
15




'''

import numpy as np

def subarrays_prod_sum(a):
    # return (np.cumsum(a) * np.cumsum(a) - a.sum())
    # return (np.cumsum(a) * np.cumsum(a) - a.sum())
    return (np.cumsum(a)**2 - np.cumsum(a) * a.sum()) / 2 # (np.cumsum(a)**2 - np.cumsum(a) * a.sum()) / 2
    
    
def all_subarrays(a):
    
    n = len(a)
    sum_all = a.sum()
    prod_all = np.prod(a)
    
    # print(sum_all, prod_all)
    
    prod_sum = subarrays_prod_sum(a)
    # print(prod_sum)
    
    if sum_all == prod_all:
        return n * (n + 1) / 2
    
    if sum_all == prod_sum:
        return n - 1
    elif prod_all == prod_sum:
        return n - 1
    
    return 0

def get_input():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = np.array(list(map(int, input().split())), dtype=np.int64)
        print(int(all_subarrays(a)))
        
if __name__ == '__main__':
    get_input()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''

# Editorial

import numpy as np

def subarrays_prod_sum(a):
    # return (np.cumsum(a) * np.cumsum(a) - a.sum())
    # return (np.cumsum(a) * np.cumsum(a) - a.sum())
    return (np.cumsum(a)**2 - np.cumsum(a) * a.sum()) / 2 # (np.cumsum(a)**2 - np.cumsum(a) * a.sum()) / 2
    
    
def all_subarrays(a):
    
    n = len(a)
    sum_all = a.sum()
    prod_all = np.prod(a)
    
    # print(sum_all, prod_all)
    
    prod_sum = subarrays_prod_sum(a)
    # print(prod_sum)
    
    if sum_all == prod_all:
        return n * (n + 1) / 2
    
    if sum_all == prod_sum:
        return n - 1
    elif prod_all == prod_sum:
        return n - 1
    
    return 0

def get_input():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = np.array(list(map(int, input().split())), dtype=np.int64)
        print(int(all_subarrays(a)))
        
if __name__ == '__main__':
    get_input()
    
'''