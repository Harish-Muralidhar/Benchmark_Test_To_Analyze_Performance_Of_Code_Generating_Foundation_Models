'''

'''

#Solution:
 
for i in range(int(input())):
    x,y,z = map(int,input().split())
    if x+y+z==180:
        print("YES")
    else:
        print("NO")