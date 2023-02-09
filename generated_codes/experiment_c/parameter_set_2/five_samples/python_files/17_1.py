"""

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def get_min_score(n, k, e, m, scores, last_exam_scores):
    # n = number of students
    # k = max number of students who get enrolled
    # e = number of exams
    # m = max number of points for a single exam
    # scores = scores for the first e-1 exams
    # last_exam_scores = scores for the last exam
    # return min score for last exam to get enrolled
    
    # get total scores for all students
    total_scores = []
    for i in range(len(scores)):
        total_scores.append(sum(scores[i]))
    
    # get min score to get enrolled
    min_score = 0
    for i in range(len(last_exam_scores)):
        total_scores[i] += last_exam_scores[i]
        total_scores.sort()
        if total_scores[n-k-1] > total_scores[n-k]:
            min_score = total_scores[n-k-1] - sum(scores[i]) + 1
            break
        else:
            min_score = m - sum(scores[i]) + 1
    
    if min_score <= 0:
        return "Impossible"
    else:
        return min_score

def main():
    # get number of test cases
    t = int(sys.stdin.readline())
    
    # get input for each test case
    for i in range(t):
        # get number of students, max number of students who get enrolled, number of exams, max number of points for a single exam
        n, k, e, m = map(int, sys.stdin.readline().split())
        
        # get scores for the first e-1 exams
        scores = []
        for j in range(n-1):
            scores.append(map(int, sys.stdin.readline().split