"""


Solution:

"""

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        print("%s=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n]) 

if __name__ == "__main__":
    t=int(input())
    while(t>0):
        n=int(input())
        m=int(input())
        arr=list(map(int,input().split()))
        subset_sum(arr, m)
        t-=1