def solution(lottos, win_nums):
    answer = []
    answer1 = []
    cnt = 0
    a = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            cnt += 1
    
    answer.append(cnt+a)
    answer.append(cnt)
    for idx,val in enumerate(answer):
        if val == 6:
            answer[idx] = 1
        elif val == 5:
            answer[idx] = 2
        elif val == 4:
            answer[idx] = 3
        elif val == 3:
            answer[idx] = 4
        elif val == 2:
            answer[idx] = 5
        elif val == 1:
            answer[idx] = 6
        elif val == 0:
            answer[idx] = 6
    return answer