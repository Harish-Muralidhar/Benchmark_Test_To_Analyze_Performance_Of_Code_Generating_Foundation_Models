"""

Note: Large Input/Output data, be careful with certain languages (though most should be OK if the algorithm is well designed)

"""


def solution(N, K, E, M, scores, last_exams):
    # init
    student = [[0] * len(scores[0])] * (N - 1)
    last_predicted_scores = [0] * (N - 1)
    total_score = [0] * (N - 1)
    last_exam_score = 0
    # read scores
    for i in range(N - 1):
        scores[i].pop()
        for j in range(len(scores[i])):
            student[i][j] = scores[i][j]
        last_predicted_scores[i] = last_exams[i]
    # calculate total scores
    for i in range(N - 1):
        for j in range(len(scores[i])):
            total_score[i] += scores[i][j]
    scores = sorted(total_score)
    needed_score = scores[K - 1] + 1
    last_exam_score = M * E - needed_score + 1

    if last_exam_score > M:
        print "Impossible"
    else:
        print last_exam_score