'''

Explanation

In the first test case the only such longest progression is (2, 4, 6).
In the second test case there are no such progressions.
In the third test case, the first 8 such progressions are (5, 14), (5, 14), (5, 14), (5, 14), (5, 14), (5, 14), (5, 14) and (5, 14).
'''

def main():
    t = int(input())
    while t:
        l,r,k,n = map(int,input().split())
        max_prog = 0
        arr = []
        for i in range(l,r+1):
            j = i+k
            ans = []
            while j <= r:
                ans.append(j)
                j += k
            if len(ans) > max_prog:
                max_prog = len(ans)
                arr = ans
        if len(arr) >= n:
            print(max_prog, arr[0], arr[1])
        else:
            print(max_prog, 0, 0)
        t -= 1
main()