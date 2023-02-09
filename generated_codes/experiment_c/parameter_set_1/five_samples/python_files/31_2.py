'''

'''


t = int(input())
for i in range(t):
    hardness, carbon_content, tensile_strength = map(float, input().split())
    
    if hardness > 50 and carbon_content < 0.7 and tensile_strength > 5600:
        print('10')
    else:
        if hardness > 50 and carbon_content < 0.7:
            print('9')
        elif carbon_content < 0.7 and tensile_strength > 5600:
            print('8')
        elif hardness > 50 and tensile_strength > 5600:
            print('7')
        elif hardness > 50 or carbon_content < 0.7 or tensile_strength > 5600:
            print('6')
        else:
            print('5')