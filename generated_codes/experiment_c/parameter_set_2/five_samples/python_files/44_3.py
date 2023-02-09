'''


'''

t=int(input())
for i in range(t):
    n,origin=input().split()
    n=int(n)
    laddu=0
    for j in range(n):
        s=input().split()
        if(s[0]=='CONTEST_WON'):
            laddu+=300
            if(int(s[1])<20):
                laddu+=20-int(s[1])
        elif(s[0]=='TOP_CONTRIBUTOR'):
            laddu+=300
        elif(s[0]=='BUG_FOUND'):
            laddu+=int(s[1])
        elif(s[0]=='CONTEST_HOSTED'):
            laddu+=50
    if(origin=='INDIAN'):
        print(laddu//200)
    else:
        print(laddu//400)