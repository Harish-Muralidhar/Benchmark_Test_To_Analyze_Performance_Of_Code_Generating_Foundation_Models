'''


'''

# Write your code here

def laddu(activity,origin):
    laddu_count = 0
    if origin == 'INDIAN':
        for i in range(activity):
            act = input().split()
            if act[0] == 'CONTEST_WON':
                rank = int(act[1])
                if rank > 20:
                    laddu_count += 300
                else:
                    laddu_count += 300 + 20 - rank
            elif act[0] == 'TOP_CONTRIBUTOR':
                laddu_count += 300
            elif act[0] == 'BUG_FOUND':
                severity = int(act[1])
                laddu_count += severity
            elif act[0] == 'CONTEST_HOSTED':
                laddu_count += 50
        if laddu_count >= 200:
            return laddu_count // 200
        else:
            return 0
    else:
        for i in range(activity):
            act = input().split()
            if act[0] == 'CONTEST_WON':
                rank = int(act[1])
                if rank > 20:
                    laddu_count += 300
                else:
                    laddu_count += 300 + 20 - rank
            elif act[0] == 'TOP_CONTRIBUTOR':
                laddu_count += 300
            elif act[0] == 'BUG_FOUND':
                severity = int(act[1])
                laddu_count += severity
            elif act[0] == 'CONTEST_HOSTED':
                laddu_count += 50
        if laddu_count >= 400:
            return laddu_count // 400
        else:
            return 0

t = int(input())
for i in range(t):
    activity,origin = input().split()
    activity = int(activity)
    print(laddu(activity,origin))