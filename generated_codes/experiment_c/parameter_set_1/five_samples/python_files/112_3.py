'''

'''

#Write code here
for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if l[i] < l[j]:
                count += 1
    print(count)