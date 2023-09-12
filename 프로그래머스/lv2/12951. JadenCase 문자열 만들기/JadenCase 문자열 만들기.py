def solution(s):
    answer = ''
    
    st = s.split(" ")
    for i in st:
        i = i.capitalize()
        if answer =="":
            answer += i
        else:
            answer = answer + " " + i
    
    return answer