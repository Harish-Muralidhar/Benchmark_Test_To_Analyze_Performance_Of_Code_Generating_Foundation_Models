"""

Explanation

Example case 1. The first phrase contains the word piygu, so it is still in use. The second phrase contains the words tefwz and piygu, so they are still in use. The third word rzotm is not used in any of the phrases, so it is not in use.

Example case 2. The only phrase contains the words kegqz, so they are still in use. The other words are not used in any of the phrases, so they are not in use.

"""

import sys

def main():
    n = int(input())
    for i in range(n):
        nk = list(map(int, input().split()))
        n = nk[0]
        k = nk[1]
        words = list(map(str, input().split()))
        phrases = []
        for i in range(k):
            l = list(map(int, input().split()))
            phrases.append(l)
        for i in range(n):
            flag = False
            for j in range(k):
                if words[i] in phrases[j]:
                    flag = True
            if flag:
                print("YES", end=" ")
            else:
                print("NO", end=" ")
        print()

if __name__ == "__main__":
    main()