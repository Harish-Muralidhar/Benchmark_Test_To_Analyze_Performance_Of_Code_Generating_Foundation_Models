'''

'''

# Write your code here

# Write your code here
t = int(input())
for i in range(t):
    n = int(input())
    s = input().split()
    s = list(s)
    count = 0
    for i in range(n):
        if len(s[i]) == 1:
            count += 1
        else:
            if s[i][0] != s[i][1]:
                count += 1
    print(count)