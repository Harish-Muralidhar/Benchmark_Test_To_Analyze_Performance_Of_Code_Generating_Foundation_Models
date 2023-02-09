'''

SAMPLE INPUT 
3
1
0 1
4
1 4
2 4
3 4
4 4
3
1 2
0 0
1 3
SAMPLE OUTPUT 
1
1
5
0000
1
101
Explanation
Example case 1. The only possible solution is that the Bytelandian is a Byteknight.

Example case 2. There are 5 possible solutions: 0000, 0001, 0010, 0011, 0111.

Example case 3. There is only one possible solution: 101.

'''

# Write your code here

def solve(n, arr):
    for i in range(n):
        if arr[i][0] == arr[i][1]:
            if arr[i][0] == 0:
                return '0'
            else:
                return '1'
    return '0'*n

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = []
        for j in range(n):
            arr.append(list(map(int, input().split())))
        print(solve(n, arr))

if __name__ == '__main__':
    main()