'''

'''

def check_subarray(arr, subarr):
    for i in range(len(arr)):
        if arr[i] == subarr[0]:
            for j in range(len(subarr)):
                if arr[i+j] != subarr[j]:
                    break
            else:
                return True
    return False

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        m = int(input())
        subarr = list(map(int, input().split()))
        if check_subarray(arr, subarr):
            print('Yes')
        else:
            print('No')