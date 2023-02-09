'''

Explanation

Example case 1. The first phrase contains the 0^th word of the dictionary, so the 0^th word is still in use. The second phrase contains the 1^th word of the dictionary, so the 1^th word is still in use. The third word is not present in any of the phrases, so it is not in use.

Example case 2. The only phrase contains the 3^th word of the dictionary, so the 3^th word is still in use. The other words are not present in the phrase, so they are not in use.

'''

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    dict = input().split()
    for k in range(K):
        L = int(input())
        phrase = input().split()
        for d in dict:
            if d in phrase:
                print("YES", end=" ")
                break
        else:
            print("NO", end=" ")
    print()