'''





'''

# cook your dish here
for _ in range(int(input())):
    k, s = input().split()
    k = int(k)
    k = 2**k
    s = list(s)
    for i in range(k):
        s[(i^(i//2))] = s[i]
    print(''.join(s))