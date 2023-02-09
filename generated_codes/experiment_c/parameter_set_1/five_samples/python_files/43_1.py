"""

"""

def kitchen(N, A, B):
    cnt=0
    for i in range(N):
        if (A[i]-B[i])>=0:
            cnt+=1
    return cnt

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        N=int(input())
        A=list(map(int, input().split()))
        B=list(map(int, input().split()))
        print(kitchen(N, A, B))