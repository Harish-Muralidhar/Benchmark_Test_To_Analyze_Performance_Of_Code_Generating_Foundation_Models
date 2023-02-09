'''

Explanation

In the first test case, Captain selected position 1 in first round. So the numbering will be [1, 0, 1, 2].

In the second test case, Captain selected position 2 in first round and 3 in second round. So the numbering will be [3, 2, 1, 1, 2, 3].

'''

def main():
    t = int(input())
    for i in range(t):
        n,m = map(int,input().split())
        arr = list(map(int,input().split()))
        ans = []
        for j in range(n):
            ans.append(0)
        for k in range(m):
            for l in range(n):
                if arr[k] > l:
                    ans[l] += 1
                else:
                    ans[l] -= 1
        print(*ans)

main()