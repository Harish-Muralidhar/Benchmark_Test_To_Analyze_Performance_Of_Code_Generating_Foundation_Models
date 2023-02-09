"""

"""

def grade_of_steel(h,cc,ts):
    grade = 0
    if h > 50 and cc < 0.7 and ts > 5600:
        return grade+10
    elif h > 50 and cc < 0.7:
        return grade+9
    elif cc < 0.7 and ts > 5600:
        return grade+8
    elif h > 50 and ts > 5600:
        return grade+7
    elif h > 50 or cc < 0.7 or ts > 5600:
        return grade+6
    else:
        return grade+5

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        h, cc, ts = map(float, input().split())
        print(grade_of_steel(h,cc,ts))