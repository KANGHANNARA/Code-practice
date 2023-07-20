def solution(food):
    answer = ''
    for idx,val in enumerate(food):
        if idx != 0:
            a = val / 2
            answer += str(idx)*int(a)
    return answer + "0" + answer[::-1]