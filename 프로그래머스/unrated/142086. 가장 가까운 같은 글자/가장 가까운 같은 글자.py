def solution(s):
    answer = []
    s_dict = dict()
    for idx,val in enumerate(s):
        if val not in s_dict:
            answer.append(-1)
            s_dict[val] = idx
        else:
            num = idx - s_dict[val]
            answer.append(num)
            s_dict[val] =idx
    return answer