'''


'''

import math
import os
import random
import re
import sys

#
# Complete the 'extinct' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. STRING_ARRAY words
#  4. 2D_STRING_ARRAY phrases
#

def extinct(n, k, words, phrases):
    # Write your code here
    for i in range(k):
        for j in range(len(phrases[i])):
            if phrases[i][j] in words:
                phrases[i][j] = 1
            else:
                phrases[i][j] = 0
    print(phrases)
    for i in range(n):
        for j in range(k):
            for h in range(len(phrases[j])):
                if words[i] == phrases[j][h]:
                    words[i] = 'YES'
                    break
    return words

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    phrases = []

    for _ in range(k):
        phrases.append(list(map(str, input().rstrip().split())))

    result = extinct(n, k, words, phrases)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()