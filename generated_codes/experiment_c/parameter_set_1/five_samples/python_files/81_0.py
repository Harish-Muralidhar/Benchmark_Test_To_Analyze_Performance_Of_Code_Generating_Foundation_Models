/*

*/

import re

def min_max(letters,sequence1,sequence2):
    temp1 = list(letters)
    temp2 = list(letters)
    
    for i in sequence1:
        temp1.insert(i,sequence1.index(i))
    for j in sequence2:
        temp2.insert(j,sequence2.index(j))
    
    temp1 = [x for x in temp1 if type(x) == str]
    temp2 = [x for x in temp2 if type(x) == str]
    
    if len(temp1) > len(temp2):
        diff = len(temp1)-len(temp2)
        temp2 = temp2 + temp1[:diff]
    elif len(temp1) < len(temp2):
        diff = len(temp2)-len(temp1)
        temp1 = temp1 + temp2[:diff]
    else:
        pass
    
    temp1 = [x for x in temp1 if re.search('[a-z]',x)]
    temp2 = [x for x in temp2 if re.search('[a-z]',x)]
    
    #print(temp1)
    #print(temp2)
    
    x = 0
    
    for i in range(len(temp1)):
        if temp1[i] == temp2[i]:
            continue
        else:
            x = x+1
    
    return x


def main():
    test_cases = int(input())
    while test_cases > 0:
        lengths = int(input())
        seq1 = [int(x) for x in input().split()]
        seq2 = [int(x) for x in input().split()]
        letters = ['A' for _ in range(0,lengths)] + ['B' for _ in range(0,lengths)]
        print(min_max(letters,seq1,seq2))
        test_cases = test_cases-1


if __name__ == '__main__':
    main()