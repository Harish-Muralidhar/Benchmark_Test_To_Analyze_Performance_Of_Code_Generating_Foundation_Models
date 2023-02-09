'''

'''

def is_possible(nums, k):
    if len(nums) == 1:
        return False
    if len(nums) == 2:
        if nums[0] == nums[1]:
            return True
        else:
            return False
    if k == 0:
        return False
    if k == 1:
        return True
    if k > 1:
        if sum(nums) % (len(nums) - 1) == 0:
            return True
        else:
            return False

def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))
        if is_possible(nums, k):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()