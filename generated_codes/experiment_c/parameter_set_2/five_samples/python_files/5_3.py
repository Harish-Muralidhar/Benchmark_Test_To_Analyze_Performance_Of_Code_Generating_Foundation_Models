'''

'''

def find_sub_string(s,f):
    for i in range(len(s)):
        if s[i]==f[0]:
            if s[i:i+len(f)]==f:
                return True
    return False

t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    f=int(input())
    f_s=list(map(int,input().split()))
    if find_sub_string(s,f_s):
        print("Yes")
    else:
        print("No")