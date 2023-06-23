def solution(a, b):
    c = str(a) + str(b)
    d = 2 * a * b
    if int(c) > d :
        answer = int(c)
    elif int(c) == d:
        answer = int(c)
    else :
        answer = int(d)
    return answer