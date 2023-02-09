'''


Explanation

Example case 1. The first phrase contains the word piygu, so the first word of the dictionary is still in use. The second phrase contains the word ezyfo, so the second word of the dictionary is still in use. The third word of the dictionary is not in use in any of the phrases.

Example case 2. The only phrase contains the word kegqz, so the fourth word of the dictionary is still in use. The other three words are not in use in any of the phrases.

'''

for _ in range(int(input())):
    n,k = map(int,input().split())
    d = set(input().split())
    for i in range(k):
        l = set(input().split()[1:])
        d = d.intersection(l)
    print(*['YES' if i in d else 'NO' for i in input().split()],sep=' ')