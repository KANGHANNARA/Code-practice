def solution(n, m, section):
    answer = 1
    a = section[0]
    for i in range(1,len(section)):
        if section[i] - a >= m:
            answer += 1
            a = section[i]
    return answer