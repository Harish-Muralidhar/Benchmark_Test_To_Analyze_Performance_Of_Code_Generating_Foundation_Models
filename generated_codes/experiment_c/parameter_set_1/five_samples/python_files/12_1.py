'''

Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.
'''
test_cases = int(input())
for i in range(test_cases):
    rooms = int(input())
    colors = input()
    red = 'R'
    green = 'G'
    blue = 'B'
    red_count = 0
    green_count = 0
    blue_count = 0
    for color in colors:
        if color==red:
            red_count+=1
        elif color==green:
            green_count+=1
        else:
            blue_count+=1
    if red_count==rooms:
        print(0)
    elif green_count==rooms:
        print(0)
    elif blue_count==rooms:
        print(0)
    else:
        if red_count>green_count and red_count>blue_count:
            print(rooms-red_count)
        elif green_count>blue_count and green_count>red_count:
            print(rooms-green_count)
        else:
            print(rooms-blue_count)