'''

Test 2 : Chef will make 2 moves: pick up the first 3 elements (4, 2 and 5), remove the largest of these (5), incurring a cost equal to the average of the other two (3), pick up the remaining two elements (3 and 2), remove the larger one (3), incurring a cost equal to the smaller one (2).

'''


import  math

def main():
    t=int(input())
    for z in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        arr.sort()
        sum=0
        while len(arr)>1:
            sum=sum+arr[0]
            arr.pop(0)
            arr.pop(0)
        print(sum)

    pass

if __name__ == '__main__':
    main()