'''


'''

import math
import os
import random
import re
import sys

# Complete the function below.

def laddu(activities):
    laddu_count = 0
    for i in range(0, activities):
        activity = input()
        activity = activity.split()
        if activity[0] == 'CONTEST_WON':
            if int(activity[1]) < 20:
                laddu_count += 300 + (20 - int(activity[1]))
            else:
                laddu_count += 300
        elif activity[0] == 'TOP_CONTRIBUTOR':
            laddu_count += 300
        elif activity[0] == 'BUG_FOUND':
            laddu_count += int(activity[1])
        elif activity[0] == 'CONTEST_HOSTED':
            laddu_count += 50
    return laddu_count


def main():
    T = int(input())
    for i in range(0, T):
        activities = int(input().split()[0])
        origin = input().split()[1]
        laddu_count = laddu(activities)
        if origin == 'INDIAN':
            print(int(laddu_count / 200))
        else:
            print(int(laddu_count / 400))


if __name__ == '__main__':
    main()