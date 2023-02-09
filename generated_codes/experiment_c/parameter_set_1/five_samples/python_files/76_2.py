"""
"""

"""
Approach:
Make a list of all people, and sort them by their x coordinates.
Now, go through that list one by one.
For every tribal clan, there is a corresponding number of people that will be added to the party.
For every dish, there is a corresponding number of people that will be removed from the party.
Keep a count of the current party size, if it ever drops below 1, we fail.
If we ever get to the end, and the party size is at least 1, we succeed.
"""

# Solution:

n = int(input())
for _ in range(n):
    x = int(input())
    b = int(input())
    b = [list(map(int, input().split())) for _ in range(b)]
    c = int(input())
    c = [list(map(int, input().split())) for _ in range(c)]
    all_events = b + c
    all_events.sort()

    added = 0
    for event in all_events:
        if len(event) == 2:
            added -= event[1]
        else:
            added += event[2]
        if added < 1:
            print(1)
            break
    else:
        print(added)