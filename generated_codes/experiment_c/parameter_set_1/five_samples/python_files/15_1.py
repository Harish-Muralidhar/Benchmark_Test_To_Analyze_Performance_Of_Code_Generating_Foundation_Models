'''
Example 3 : Cops in house 10 can cover houses 1 to 15, and cops in house 51 can cover houses 40 to 90, leaving houses numbered 16 to 39, and 91 to 100 safe. So, in total 19 houses are safe.
'''
def split(text):
    return [char for char in text]

def my_func(M, x, y, cops):
    #cops = cops.split()
    cops = list(map(int, cops))
    #print(cops)
    safe_houses = []
    for house in range(1, 101):
        safe = True
        for cop in cops:
            if house in range(cop - (x * y), cop + (x * y) + 1):
                #print(house, 'in', range(cop - (x * y), cop + (x * y) + 1))
                safe = False
                break
        if safe:
            safe_houses.append(house)
    #print(safe_houses)
    return len(safe_houses)

T = int(input())
output = []
for t in range(T):
    M, x, y = input().split()
    cops = input()
    output.append(my_func(M, int(x), int(y), cops))
print('\n'.join(list(map(str, output))))