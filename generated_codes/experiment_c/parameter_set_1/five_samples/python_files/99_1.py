'''

A subsequence of a sequence is a sequence that can be derived from the original sequence by deleting some elements without changing the order of the remaining elements. 

A contiguous subsequence is a subsequence where the elements appear in order in the original sequence.
'''

def main():
    testcases = int(input())
    for _ in range(testcases):
        n = int(input())
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        dic = {}
        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] = [i]
            else:
                dic[arr[i]].append(i)
        max_len = 0
        for i in range(len(brr)):
            if len(dic[brr[i]]) > 1:
                max_len = max(max_len, 1)
            if len(dic[brr[i]]) == 1:
                if brr[i] == arr[i]:
                    continue
                min_index = dic[brr[i]][0]
                max_index = dic[brr[i]][0]
                curr = brr[i]
                while True:
                    if curr == arr[min_index]:
                        break
                    if curr not in dic:
                        break
                    if len(dic[curr]) == 0:
                        break
                    min_index = min(min_index, dic[curr][0])
                    max_index = max(max_index, dic[curr][0])
                    curr = arr[min_index]
                if curr == arr[min_index]:
                    max_len = max(max_len, max_index - min_index + 1)
        print(max_len)
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
if __name__ == '__main__':
    main()