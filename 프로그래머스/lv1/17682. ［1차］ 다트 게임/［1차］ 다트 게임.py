def solution(dartResult):
    answer = []
    num = ''
    for i in dartResult:
        if i.isnumeric():
            num += i
        elif i == "S":
            num = int(num)
            answer.append(num)
            num = ''
        elif i == "D":
            num = int(num)**2
            answer.append(num)
            num = ''
        elif i == "T":
            num = int(num)**3
            answer.append(num)
            num = ''
        elif i == "*":
            if len(answer) > 1:
                answer[-2] = answer[-2] * 2
                answer[-1] = answer[-1] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif i == "#":
            answer[-1] = answer[-1] * (-1)
    return sum(answer)