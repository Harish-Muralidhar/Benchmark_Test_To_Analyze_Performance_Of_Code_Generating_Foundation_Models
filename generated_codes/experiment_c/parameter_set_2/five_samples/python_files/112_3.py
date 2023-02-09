'''

'''

def count_pairs(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]<numbers[j]:
                count += 1
    return count

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        numbers = [int(i) for i in input().split()][0:n]
        print(count_pairs(numbers))