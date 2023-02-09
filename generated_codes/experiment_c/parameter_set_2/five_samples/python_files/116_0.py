'''

'''

import math

def count_subsequences(numbers):
    numbers.sort()
    #print(numbers)
    if len(numbers) == 1:
        return 1
    if len(numbers) == 2:
        return 3
    if numbers[0] == numbers[-1]:
        return int(math.pow(2, len(numbers)) - 1)
    else:
        return int(math.pow(2, len(numbers) - 1) - 1)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        numbers = list(map(int, input().split()))
        print(count_subsequences(numbers))

if __name__ == "__main__":
    main()