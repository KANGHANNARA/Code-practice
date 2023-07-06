def solution(num_list):
    answer = 0
    a = 0
    b = 0
    for i in range(0,len(num_list),2):
        a += num_list[i]
    for i in range(1,len(num_list),2):
        b += num_list[i]
    if a > b :
        answer = a
    elif a < b :
        answer = b
    else:
        answer = a
    return answer