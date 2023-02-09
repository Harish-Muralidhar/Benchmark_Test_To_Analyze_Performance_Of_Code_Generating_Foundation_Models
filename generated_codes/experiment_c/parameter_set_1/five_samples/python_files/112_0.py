'''

Input:
2
2
2 1
3
3 1 2

Output:
1
3

Explanation:
Testcase 1: Only one such pair: (2,1).
Testcase 2: 3 possible pairs: (2,1), (2,3), (3,1)

'''
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(set(a))
    b.sort()
    c = a.count(b[0])
    res = 0
    for i in range(1,len(b)):
        val = a.count(b[i])
        if(c>=val):
            res += val
            c = val
        else:
            res += c
            c = val
    print(res)