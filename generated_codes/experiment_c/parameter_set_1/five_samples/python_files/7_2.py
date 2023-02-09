'''

In the third example,
You will have to paint 2 balloons to make all the balloons of the same color.

'''

def min_flip(str1):
    str1 = list(str1)
    count = 0
    for i in range(len(str1)):
        if str1[i] == 'a':
            count += 1
    return min(count, len(str1)-count)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        str1 = input()
        print(min_flip(str1))