'''

'''

t = int(input())

for i in range(t):
    n = input()
    sum1 = 0
    for j in n:
        sum1 = sum1 + int(j)
    print(sum1)

#method 2
# t = int(input())
#
# for i in range(t):
#     n = input()
#     sum1 = 0
#     for j in range(len(n)):
#         sum1 = sum1 + int(n[j])
#     print(sum1)