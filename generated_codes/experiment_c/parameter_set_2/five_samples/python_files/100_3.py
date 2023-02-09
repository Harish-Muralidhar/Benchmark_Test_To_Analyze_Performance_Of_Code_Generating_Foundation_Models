"""


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

def main():
    t = int(input())
    for i in range(t):
        n,m = map(int,input().split())
        arr = list(map(int,input().split()))
        subset_sum(arr,m)

if __name__ == "__main__":
    main()