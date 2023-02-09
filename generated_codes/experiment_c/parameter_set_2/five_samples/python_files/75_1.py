'''

'''

def check(nums,k):
    nums.sort()
    if nums[0]==0:
        return False
    for i in range(1,len(nums)):
        if nums[i]==0:
            return False
        if nums[i]>nums[i-1]+k:
            return False
    return True

def main():
    T=int(input())
    for _ in range(T):
        n,k=map(int,input().split())
        nums=list(map(int,input().split()))
        if check(nums,k):
            print("YES")
        else:
            print("NO")

main()