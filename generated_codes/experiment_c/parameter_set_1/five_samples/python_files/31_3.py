'''

'''

# Write your code here
n = int(input())
for i in range(n):
    hardness, carbon, t_strength = map(float, input().split())
    if hardness > 50 and carbon < 0.7 and t_strength > 5600:
        print('10')
    elif hardness > 50 and carbon < 0.7:
        print('9')
    elif carbon < 0.7 and t_strength > 5600:
        print('8')
    elif hardness > 50 and t_strength > 5600:
        print('7')
    elif hardness > 50 or carbon < 0.7 or t_strength > 5600:
        print('6')
    else:
        print('5')