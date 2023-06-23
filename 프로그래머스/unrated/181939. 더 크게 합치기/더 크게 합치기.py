def solution(a, b):
    c = str(a) + str(b)
    d = str(b) + str(a)
    if c > d :
        answer = int(c)
    else :
        answer = int(d)
    return answer