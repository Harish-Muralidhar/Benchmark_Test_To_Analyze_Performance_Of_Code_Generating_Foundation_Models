'''

'''

# Write your code here

def get_min_max_diff(str1, str2):
    min_diff = 0
    max_diff = 0
    for i in range(len(str1)):
        if str1[i] != '?' and str2[i] != '?':
            if str1[i] != str2[i]:
                min_diff += 1
                max_diff += 1
        elif str1[i] == '?' and str2[i] == '?':
            max_diff += 1
        else:
            max_diff += 1
            min_diff += 1
    return min_diff, max_diff

if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        str1 = input()
        str2 = input()
        min_diff, max_diff = get_min_max_diff(str1, str2)
        print(min_diff, max_diff)