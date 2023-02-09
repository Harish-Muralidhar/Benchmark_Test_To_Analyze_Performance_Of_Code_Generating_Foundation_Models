'''


========================================================================================



'''

def func(n,k,dictionary,phrases):
    ans = []
    for i in range(n):
        flag = 0
        for key in phrases:
            for j in key:
                if dictionary[i] == j:
                    flag = 1
                    break
            if flag == 1:
                ans.append('YES')
                break
        if flag == 0:
            ans.append('NO')
    print(*ans)

T = int(input())
for i in range(T):
    n,k = map(int,input().split())
    dictionary = input().split()
    phrases = {}
    for i in range(k):
        temp = input().split()
        phrases[temp[0]] = temp[1:]
    func(n,k,dictionary,phrases)