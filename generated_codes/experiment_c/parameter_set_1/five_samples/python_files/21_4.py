"""

"""

#CODE
a=int(input())
list1=[]
for i in range(0,a):
    list2=[]
    b=input().split(" ")
    list2.append(b[0])
    list2.append(b[1])
    list1.append(list2)
for i in list1:
    c=int(i[0])%int(i[1])
    print(c)