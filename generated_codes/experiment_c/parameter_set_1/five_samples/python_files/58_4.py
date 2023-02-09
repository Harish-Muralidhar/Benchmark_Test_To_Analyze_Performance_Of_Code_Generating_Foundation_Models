'''


'''

#t = int(input())
#for _ in range(t):
#    n,m = list(map(int, input().split()))
#    a = list(map(int, input().split()))

n,m = 6,10
a = [4,4,4,4,4,4]

#n,m = 6,3
#a = [4,4,4,4,4,4]

#n,m = 5,8
#a = [1,1,1,1,128]

#n,m = 7,4
#a = [4,5,6,7,8,9,10]

t = 0
for i in range(n):
    t += a[i]

def get_num(n,m):
    if m==0:
        return 1
    else:
        return 2*get_num(n, m-1)

def get_combs(n,m,t,a):
    if n==1:
        if t&(1<<(m-1))==0:
            return 1
        else:
            return 0
    else:
        combs = 0
        for i in range(n):
            for j in range(1,n-i+1):
                t1 = sum(a[i:i+j])
                t2 = sum(a[i+j:])
                if t1&(1<<(m-1))==0 and t2&(1<<(m-1))==0:
                    combs += get_combs(i,m,t1,a[:i])*get_combs(n-i-j,m,t2,a[i+j:])
        return combs

combs = get_combs(n,m,t,a)
#combs = get_combs(3,2,8,[1,2,5])
#combs = get_combs(1,2,2,[2])
print(combs)