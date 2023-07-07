def solution(s):
    answer = 0
    for i in s:
        if i == "(":
            answer +=1
        else:
            if answer > 0:
                answer -= 1
            else:
                return False
    if answer > 0:
        return False
    return True