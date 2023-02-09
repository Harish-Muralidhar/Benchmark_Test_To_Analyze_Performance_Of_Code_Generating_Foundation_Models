'''

'''

# Write your code here
for i in range(int(input())):
    l=[]
    count=0
    for j in range(int(input().split()[0])):
        l.append(input().split())
    for k in range(len(l)):
        if l[k][0]=="CONTEST_WON":
            count+=300
            if int(l[k][1])<20:
                count+=20-int(l[k][1])
        elif l[k][0]=="TOP_CONTRIBUTOR":
            count+=300
        elif l[k][0]=="BUG_FOUND":
            count+=int(l[k][1])
        elif l[k][0]=="CONTEST_HOSTED":
            count+=50
    if input().split()[1]=="INDIAN":
        print(count//200)
    else:
        print(count//400)