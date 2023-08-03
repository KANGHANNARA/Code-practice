def solution(N, stages):
    a = len(stages)
    b = []
    answer = []
    for i in range(1,N+1):
        cnt = 0
        for j in stages:
            if i == j:
                cnt +=1
        if cnt == 0:
            b.append(0)
        else:
            b.append(cnt/a)
        a = a-cnt
    c = sorted(b, reverse=True)
    for i in range(len(b)):
        answer.append(b.index(c[i])+1)
        b[b.index(c[i])]=2
    return answer