'''

'''

#code

import numpy as np

def check_grade(hardness, carbon, tensile_strength):
    if hardness > 50 and carbon < 0.7 and tensile_strength > 5600:
        return 10
    elif hardness > 50 and carbon < 0.7:
        return 9
    elif carbon < 0.7 and tensile_strength > 5600:
        return 8
    elif hardness > 50 and tensile_strength > 5600:
        return 7
    elif hardness > 50 or carbon < 0.7 or tensile_strength > 5600:
        return 6
    else:
        return 5

t = int(input())
for i in range(t):
    hardness, carbon, tensile_strength = map(float, input().split())
    print(check_grade(hardness, carbon, tensile_strength))