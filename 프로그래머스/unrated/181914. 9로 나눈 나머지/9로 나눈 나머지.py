def solution(number):
    answer = 0
    for i in list(map(int, str(number))):
        answer += i
    return answer%9