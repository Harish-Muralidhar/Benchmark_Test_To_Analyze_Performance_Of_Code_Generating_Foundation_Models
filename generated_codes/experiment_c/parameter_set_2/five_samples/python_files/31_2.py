"""

"""

import sys

def grade(hardness, carbon, strength):
    if hardness > 50 and carbon < 0.7 and strength > 5600:
        return 10
    elif hardness > 50 and carbon < 0.7:
        return 9
    elif carbon < 0.7 and strength > 5600:
        return 8
    elif hardness > 50 and strength > 5600:
        return 7
    elif hardness > 50 or carbon < 0.7 or strength > 5600:
        return 6
    else:
        return 5

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        hardness, carbon, strength = map(float, input().split())
        print(grade(hardness, carbon, strength))