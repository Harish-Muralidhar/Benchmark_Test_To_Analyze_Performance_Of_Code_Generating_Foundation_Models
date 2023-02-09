'''


'''

def hamming_distance(str1,str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count

def max_hamming_distance(str1,str2):
    max_hamming = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if str1[i] == 'W':
                str1[i] = 'B'
            else:
                str1[i] = 'W'
            hamming = hamming_distance(str1,str2)
            if hamming > max_hamming:
                max_hamming = hamming
            if str1[i] == 'W':
                str1[i] = 'B'
            else:
                str1[i] = 'W'
    return max_hamming

def max_hamming_distance_lexicographically(str1,str2):
    max_hamming = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if str1[i] == 'W':
                str1[i] = 'B'
            else:
                str1[i] = 'W'
            hamming = hamming_distance(str1,str2)
            if hamming > max_hamming:
                max_hamming = hamming
                lexicographically_smallest = str1
            if str1[i] == 'W':
                str1[i] = 'B'
            else:
                str1[i] = 'W'
    return lexicographically_smallest

def main():
    t = int(input())
    while t > 0:
        str1 = list(input())
        str2 = list(input())
        print(''.join(max_hamming_distance_lexicographically(str1,str2)))
        t -= 1

if __name__ == '__main__':
    main()