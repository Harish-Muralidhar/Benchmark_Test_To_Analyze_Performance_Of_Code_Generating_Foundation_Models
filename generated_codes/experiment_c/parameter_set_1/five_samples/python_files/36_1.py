'''

Explanation

In the first case, both the first and the second words exist in the modern language phrases.
In the second case, none of the words exists in modern phrases. 

'''

import re

def isExist(a, b):
    for i in range(len(a)):
        if a[i] in b:
            return True
    return False


def main():
    testCase = int(input())

    while(testCase > 0):
        nk = list(map(int, input().split()))
        n = nk[0]
        k = nk[1]

        dic = list(map(str, input().split()))
        output = []

        for i in range(k):
            l = int(input())
            m = list(map(str, input().split()))
            output.append(isExist(m, dic))

        for j in range(n):
            if output[j]:
                print("YES", end = " ")
            else:
                print("NO", end = " ")
        print()
        testCase -= 1

if __name__ == "__main__":
    main()