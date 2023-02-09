"""

"""

# t = int(input())
# for _ in range(t):
#     s = input()
#     l = len(s)
#     for i in range(l-1):
#         for j in range(i+1,l):
#             if s[i] == s[j]:
#                 print(s[i])
#                 break
#         break
#     else:
#         print(-1)

# t = int(input())
# for _ in range(t):
#     s = input()
#     l = len(s)
#     for i in range(l-1):
#         if s[i] == s[i+1]:
#             print(s[i])
#             break
#     else:
#         print(-1)

t = int(input())
for _ in range(t):
    s = input()
    l = len(s)
    for i in range(l-1):
        if s[i] == s[i+1]:
            print(s[i])
            break
    else:
        print(-1)