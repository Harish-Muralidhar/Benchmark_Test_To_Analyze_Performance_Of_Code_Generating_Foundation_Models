"""

"""


# Write your code here

def main():
    N, M = [int(x) for x in input().strip().split()]
    arr = [int(x) for x in input().strip()]
    arr = arr[0:N]
    while M > 0:
        x = int(input())
        # Logic
        indx = 0
        b1 = 0
        b2 = 0
        while indx < x:
            val = arr[x - 1] - arr[indx]
            if val > 0:
                b1 += val
            else:
                b2 += val
            indx += 1
        print(b1 + b2)
        M -= 1


main()