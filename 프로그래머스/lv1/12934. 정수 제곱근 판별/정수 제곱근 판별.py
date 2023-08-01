def solution(n):
    answer = 0
    if (n**(1/2)).is_integer() == True:
        answer = ((n **(1/2))+1)**2
    else:
        answer = -1
    return answer