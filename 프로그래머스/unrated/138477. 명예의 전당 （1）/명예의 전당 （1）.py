def solution(k, score):
    answer = []
    score_honor = []
    
    for i in range(len(score)):
        score_honor.append(score[i])
        score_honor.sort()
        answer.append(min(score_honor[-k:]))
    return answer