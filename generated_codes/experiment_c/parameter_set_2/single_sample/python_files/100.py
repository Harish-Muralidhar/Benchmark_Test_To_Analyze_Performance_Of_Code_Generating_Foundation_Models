'''


'''

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    if s == target: 
        return partial
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
        numbers = list(map(int,input().split()))
        result = subset_sum(numbers, m)
        if result is None:
            print("No")
        else:
            print("Yes")

if __name__ == "__main__":
    main()