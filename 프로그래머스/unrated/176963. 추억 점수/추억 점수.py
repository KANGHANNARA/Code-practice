def solution(name, yearning, photo):
    answer = []
    n_dict = dict(zip(name,yearning))
    for i in photo:
        a = 0
        for j in i:
            if j in name:
                a += n_dict[j]
        answer.append(a)
    return answer