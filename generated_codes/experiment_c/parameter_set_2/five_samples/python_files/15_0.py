'''
Example 3 : Cops in house 10 can cover houses 1 to 18, and cops in house 51 can cover houses 41 to 91, leaving houses numbered 19 to 40, and 92 to 100 safe. So, in total 9 houses are safe.

'''

import math

def safe_houses(m,x,y,houses):
    safe_houses = []
    for i in range(1,101):
        if i not in houses:
            safe_houses.append(i)
    return safe_houses

def max_distance(x,y):
    return x*y

def safe_houses_count(safe_houses,max_distance):
    count = 0
    for i in range(len(safe_houses)):
        if i == 0:
            if safe_houses[i] <= max_distance:
                count += 1
        else:
            if safe_houses[i] - safe_houses[i-1] <= max_distance:
                count += 1
    return count

def main():
    t = int(input())
    for i in range(t):
        m,x,y = map(int,input().split())
        houses = list(map(int,input().split()))
        safe_houses = safe_houses(m,x,y,houses)
        max_distance = max_distance(x,y)
        safe_houses_count = safe_houses_count(safe_houses,max_distance)
        print(safe_houses_count)

if __name__ == '__main__':
    main()