'''

'''

# Write your code here

def laddu(activities, origin):
    laddus = 0
    for activity in activities:
        if activity[0] == 'CONTEST_WON':
            laddus += 300
            if int(activity[1]) < 20:
                laddus += 20 - int(activity[1])
        elif activity[0] == 'TOP_CONTRIBUTOR':
            laddus += 300
        elif activity[0] == 'BUG_FOUND':
            laddus += int(activity[1])
        elif activity[0] == 'CONTEST_HOSTED':
            laddus += 50
    if origin == 'INDIAN':
        return laddus // 200
    else:
        return laddus // 400

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, origin = input().split()
        N = int(N)
        activities = [input().split() for _ in range(N)]
        print(laddu(activities, origin))