def solution(s):
    answer = []
    s_dict = dict()
    for idx,val in enumerate(s):
        if val not in s_dict: # s_dict에 없는 값은 answer에 -1 
            answer.append(-1)
            s_dict[val] = idx # val값에 인덱스 값 수정
        else:
            num = idx - s_dict[val] # 인덱스값에서 s_dict에 있는 인덱스 값 빼기(거리 계산)
            answer.append(num)
            s_dict[val] =idx # val값에 인덱스 값 수정
    return  answer