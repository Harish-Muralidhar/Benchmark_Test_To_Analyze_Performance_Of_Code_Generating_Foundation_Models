'''

'''

# Write your code here
def is_possible(n,k,arr):
    for i in range(n):
        if abs(arr[i]-i)<k:
            return False
    return True

def find_min(n,k,arr):
    for i in range(n):
        if abs(arr[i]-i)<k:
            arr[i]=i+k
    return arr

def main():
    t=int(input())
    while t>0:
        n,k=map(int,input().split())
        arr=list(map(int,input().split()))
        if is_possible(n,k,arr):
            arr=find_min(n,k,arr)
            print(*arr)
        else:
            print(-1)
        t-=1

if __name__ == '__main__':
    main()