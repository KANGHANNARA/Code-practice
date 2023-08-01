def solution(x):
    answer = []
    for i in str(x):
        answer.append(int(i))
        
    return True if x % sum(answer) == 0 else False