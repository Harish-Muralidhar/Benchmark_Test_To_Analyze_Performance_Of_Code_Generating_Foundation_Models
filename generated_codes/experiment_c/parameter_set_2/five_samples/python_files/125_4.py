'''
Example case 2. Game will have 2 turns. In first turn Sasha will choose 2, while Chef will choose 3. In second turn Sasha will choose 4, while Chef will choose 1. Hence answer is 1.5. 
Example case 3. Game will have 2 turns. In first turn Sasha will choose 2, while Chef will choose 2. In second turn Sasha will choose 2, while Chef will choose 2. Hence answer is 0. 

'''

import random

def calculate_probability(a,b):
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]**b[j] > b[j]**a[i]:
                count += 1
    return count/len(a)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        print(calculate_probability(a,b))

if __name__ == '__main__':
    main()