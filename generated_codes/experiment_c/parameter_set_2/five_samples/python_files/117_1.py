'''

Explanation
Test Case 1:

After round 1, the numbering will be [1, 0, 1, 2]

Test Case 2:

After round 1, the numbering will be [3, 2, 1, 1, 2, 3]
After round 2, the numbering will be [2, 1, 0, 1, 2, 3]

'''

def max_number(n,m,positions):
    max_number = 0
    for i in range(n):
        count = 0
        for j in range(m):
            if i >= positions[j]:
                count += 1
            else:
                count += (positions[j] - i)
        if count > max_number:
            max_number = count
    return max_number

def main():
    T = int(input())
    for i in range(T):
        n,m = map(int,input().split())
        positions = list(map(int,input().split()))
        print(max_number(n,m,positions))
        
if __name__ == '__main__':
    main()