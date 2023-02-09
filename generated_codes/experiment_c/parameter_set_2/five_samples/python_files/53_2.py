'''

'''

import itertools

def check_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

def get_combinations(string_list):
    combinations_list = []
    for i in range(1,len(string_list)+1):
        combinations_list.extend(list(itertools.combinations(string_list,i)))
    return combinations_list

def get_min_deletions(string_list):
    combinations_list = get_combinations(string_list)
    for combination in combinations_list:
        string = ''.join(combination)
        if check_palindrome(string):
            return len(string_list) - len(combination)
    return len(string_list)

if __name__ == '__main__':
    test_cases = int(input())
    for test_case in range(test_cases):
        string_list = list(input().split())
        print(get_min_deletions(string_list))