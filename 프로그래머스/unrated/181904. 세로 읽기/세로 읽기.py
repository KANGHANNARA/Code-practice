def solution(my_string, m, c):
    a = [my_string[i:i+m] for i in range(0, len(my_string), m)]
    answer = "".join([a[i][c-1] for i in range(0, len(a))])
    return answer