'''

'''

import numpy as np

def grade(hardness, carbon, tensile):
    if hardness > 50 and carbon < 0.7 and tensile > 5600:
        return 10
    elif hardness > 50 and carbon < 0.7:
        return 9
    elif carbon < 0.7 and tensile > 5600:
        return 8
    elif hardness > 50 and tensile > 5600:
        return 7
    elif hardness > 50 or carbon < 0.7 or tensile > 5600:
        return 6
    else:
        return 5

if __name__ == "__main__":
    num_tests = int(input())
    for i in range(num_tests):
        hardness, carbon, tensile = map(float, input().split())
        print(grade(hardness, carbon, tensile))