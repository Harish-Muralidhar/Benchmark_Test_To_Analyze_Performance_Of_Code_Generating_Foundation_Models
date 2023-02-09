'''

'''

#ANSWER

for _ in range(int(input())):
    activity, origin = input().split()
    
    activity = int(activity)
    laddu = 0
    for __ in range(activity):
        value = input().split()
        
        if value[0] == 'CONTEST_WON':
            laddu += 300
            if int(value[1]) < 20:
                laddu += 20 - int(value[1])
        elif value[0] == 'TOP_CONTRIBUTOR':
            laddu += 300
        elif value[0] == 'BUG_FOUND':
            laddu += int(value[1])
        elif value[0] == 'CONTEST_HOSTED':
            laddu += 50
            
    if origin == 'INDIAN':
        print(laddu // 200)
    else:
        print(laddu // 400)