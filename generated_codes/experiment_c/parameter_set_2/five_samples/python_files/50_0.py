'''


'''


def count_substring(string):
    count = 0
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            if string[i:j].count('A') == string[i:j].count('B') == string[i:j].count('C'):
                count += 1
    return count


print(count_substring('ABACABA'))