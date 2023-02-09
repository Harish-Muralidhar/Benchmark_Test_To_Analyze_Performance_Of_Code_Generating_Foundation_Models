'''


'''

# cook your dish here

# t = int(input())
# while(t>0):
#     t-=1
#     a,b = map(int, input().split())
#     z = 0
#     while(b>a):
#         z+=1
#         b=b//2
#     while(b<a):
#         z+=1
#         b = b*2
#     print(z)

# t = int(input())
# while(t>0):
#     t-=1
#     a,b = map(int, input().split())
#     z = 0
#     if(a==b):
#         print(z)
#     elif(a<b):
#         while(b>a):
#             z+=1
#             b=b//2
#         while(b<a):
#             z+=1
#             b = b*2
#         print(z)
#     else:
#         if(a>b):
#             while(a>b):
#                 z+=1
#                 a=a//2
#             while(b>a):
#                 z+=1
#                 b=b//2
#             print(z)

t = int(input())
while(t>0):
    t-=1
    a,b = map(int, input().split())
    z = 0
    if(a==b):
        print(z)
    elif(a<b):
        while(b>a):
            z+=1
            b=b//2
        while(b<a):
            z+=1
            b = b*2
        print(z)
    else:
        while(a>b):
            z+=1
            a=a//2
        while(b>a):
            z+=1
            b=b//2
        print(z)