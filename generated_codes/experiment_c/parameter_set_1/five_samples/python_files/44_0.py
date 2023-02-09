"""

"""

for _ in range(int(input())):
    no_of_activities, origin = input().split()
    no_of_activities = int(no_of_activities)

    laddus = 0
    for i in range(no_of_activities):
        activity = input().split()
        
        if activity[0] == "CONTEST_WON":
            rank = int(activity[1])
            laddus += 300
            if rank < 20:
                laddus += 20 - rank
        
        elif activity[0] == "TOP_CONTRIBUTOR":
            laddus += 300
        
        elif activity[0] == "BUG_FOUND":
            laddus += int(activity[1])
        
        elif activity[0] == "CONTEST_HOSTED":
            laddus += 50
        
    if origin == "INDIAN":
        print(laddus // 200)
    
    else:
        print(laddus // 400)