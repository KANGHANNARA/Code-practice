def solution(num_list):
    answer = []
    a = num_list[-1]
    b = num_list[-2]
    if a > b:
        answer.extend(num_list)
        answer.append(a-b)
    else :
        answer.extend(num_list)
        answer.append(a*2)
        
    return answer