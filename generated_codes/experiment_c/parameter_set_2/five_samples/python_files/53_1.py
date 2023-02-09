'''

'''

def check(s):
    if s==s[::-1]:
        return True
    else:
        return False

def main():
    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(str,input().split()))
        c=0
        for i in l:
            if len(i)==1:
                c+=1
            else:
                if check(i)==False:
                    c+=1
        print(c)

if __name__=='__main__':
    main()