'''

'''

def main():
    t = int(input())
    while t > 0:
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(find_min(arr))
        t -= 1

def find_min(arr):
    min_val = min(arr)
    for i in range(len(arr)):
        arr[i] -= min_val
    return min_val

if __name__ == "__main__":
    main()