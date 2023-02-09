'''


'''



# Write your code here
for i in range(int(input())):
    a,b = map(int,input().split())
    mat = []
    for j in range(a):
        mat.append(list(map(int,input())))
    cnt = 0
    for j in range(b):
        k = 0
        for l in range(a):
            if mat[l][j] == 1:
                k += 1
        if k > 1:
            cnt += (k*(k-1))//2
    print(cnt)