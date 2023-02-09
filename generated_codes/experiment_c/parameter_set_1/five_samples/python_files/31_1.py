'''

'''

a = 0
b = 0
c = 0
for i in range(3):
    
    temp = input()
    temp = temp.split()
    temp = [int(x) for x in temp]
    if temp[0]>50:
        a+=1
    if temp[1]<0.7:
        b+=1
    if temp[2]>5600:
        c+=1
    
    if(a == 1 and b == 1 and c == 1):
        print("10")
    elif(a == 0 and b == 1 and c == 1):
        print("8")
    elif(a == 1 and b == 0 and c == 1):
        print("7")
    elif(a == 1 and b == 1 and c == 0):
        print("9")
    elif(a == 0 and b == 0 and c == 0):
        print("5")
    else:
        print("6")