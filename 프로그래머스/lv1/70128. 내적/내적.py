def solution(a, b):
    answer = 0
    for i,x in zip(a,b):
        answer += i*x
    return answer