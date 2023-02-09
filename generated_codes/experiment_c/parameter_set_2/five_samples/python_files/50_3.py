'''


'''

def count_substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if is_valid(s[i:j+1]):
                count += 1
    return count

def is_valid(s):
    return (len(s) == len(set(s)))

if __name__ == '__main__':
    s = input()
    print(count_substrings(s))