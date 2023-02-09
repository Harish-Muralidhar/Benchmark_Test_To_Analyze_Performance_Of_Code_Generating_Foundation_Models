"""

"""

def xorSum(arr,n):
    xor = 0
    for i in range(n):
        xor ^= arr[i]
    return xor

def countPossibleSets(arr,xor,n):
    count = 0
    for i in range(n):
        if arr[i] >= xor:
            count += 1
    return count

def xorSumOfAllSets(arr,n):
    xor = xorSum(arr,n)
    count = countPossibleSets(arr,xor,n)
    return count

def main():
    t = int(input())
    while t > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(xorSumOfAllSets(arr,n))
        t -= 1


if __name__ == "__main__":
    main()