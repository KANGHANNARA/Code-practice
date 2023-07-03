def solution(my_string, is_prefix):
    answer = 0
    start = [my_string[:i] for i in range(0, len(my_string))]
    if is_prefix in start:
        answer = 1
    else:
        answer = 0
    return answer