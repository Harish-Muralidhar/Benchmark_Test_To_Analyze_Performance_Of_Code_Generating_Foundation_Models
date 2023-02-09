'''

'''

import sys

def grade_of_steel(hardness, carbon_content, tensile_strength):
    if hardness > 50 and carbon_content < 0.7 and tensile_strength > 5600:
        return 10
    elif hardness > 50 and carbon_content < 0.7:
        return 9
    elif carbon_content < 0.7 and tensile_strength > 5600:
        return 8
    elif hardness > 50 and tensile_strength > 5600:
        return 7
    elif hardness > 50 or carbon_content < 0.7 or tensile_strength > 5600:
        return 6
    else:
        return 5

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        hardness, carbon_content, tensile_strength = [float(i) for i in input().split()]
        print(grade_of_steel(hardness, carbon_content, tensile_strength))