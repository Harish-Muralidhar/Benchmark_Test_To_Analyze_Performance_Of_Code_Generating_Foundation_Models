"""


"""

def subarray_sum_product(arr):
    subarray_count = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sum = 0
            product = 1
            for k in range(i, j+1):
                sum += arr[k]
                product *= arr[k]
            if sum == product:
                subarray_count += 1
    return subarray_count

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(subarray_sum_product(arr))

if __name__ == "__main__":
    main()