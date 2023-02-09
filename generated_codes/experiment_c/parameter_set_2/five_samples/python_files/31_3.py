'''

'''

# Write your code here

# Write your code here
import numpy as np

def steel_grade(hardness, carbon, tensile):
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

T = int(input())

for i in range(T):
    hardness, carbon, tensile = map(float, input().split())
    print(steel_grade(hardness, carbon, tensile))