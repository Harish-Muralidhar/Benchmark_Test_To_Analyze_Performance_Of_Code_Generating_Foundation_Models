'''


'''

def laddu(origin, activities):
    laddu = 0
    for i in range(activities):
        activity = input().split()
        if activity[0] == 'CONTEST_WON':
            laddu += 300
            if int(activity[1]) < 20:
                laddu += (20 - int(activity[1]))
        elif activity[0] == 'TOP_CONTRIBUTOR':
            laddu += 300
        elif activity[0] == 'BUG_FOUND':
            laddu += int(activity[1])
        elif activity[0] == 'CONTEST_HOSTED':
            laddu += 50
    if origin == 'INDIAN':
        return laddu // 200
    else:
        return laddu // 400

test_cases = int(input())
for i in range(test_cases):
    activities, origin = input().split()
    print(laddu(origin, int(activities)))