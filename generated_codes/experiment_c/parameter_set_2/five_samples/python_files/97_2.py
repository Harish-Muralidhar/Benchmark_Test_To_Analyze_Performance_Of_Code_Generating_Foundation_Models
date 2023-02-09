"""

"""

def find_min(arr):
    min_val = arr[0]
    min_index = 0
    for i in range(1,len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_index = i
    return min_index

def find_max(arr):
    max_val = arr[0]
    max_index = 0
    for i in range(1,len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
    return max_index

def find_sum(arr):
    return sum(arr)

def find_winner(arr,N,M):
    alice_sum = 0
    bob_sum = 0
    while(N>0 and M>0):
        if N>1 and M>1:
            if N>M:
                alice_sum += find_sum(arr[0])
                arr.pop(0)
                N -= 1
                bob_sum += find_sum(arr[N-1])
                arr.pop(N-1)
                N -= 1
            else:
                alice_sum += find_sum(arr[0])
                arr.pop(0)
                M -= 1
                bob_sum += find_sum(arr[M-1])
                arr.pop(M-1)
                M -= 1
        elif N==1 and M>1:
            alice_sum += find_sum(arr[0])
            arr.pop(0)
            M -= 1
            bob_sum += find_sum(arr[M-1])
            arr.pop(M-1)
            M -= 1
        elif N>1 and M==1:
            alice_sum += find_sum(arr[0])
            arr.pop(0)
            N -= 1
            bob_sum += find_sum(arr[N-1])
            arr.pop(N-1)
            N -= 1
        else:
            alice_