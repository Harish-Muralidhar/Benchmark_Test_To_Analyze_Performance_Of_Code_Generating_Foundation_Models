"""
"""

def kitchen_timetable(A,B):
    n = len(A)
    count = 0
    for i in range(n):
        if B[i] <= A[i] - A[i-1]:
            count += 1
    return count

t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print (kitchen_timetable(A,B))