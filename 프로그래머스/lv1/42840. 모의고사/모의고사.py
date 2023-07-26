def solution(answers):
    result = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0,0,0]
    
    for idx,val in enumerate(answers):
        if val == a1[idx%5]:
            score[0] += 1
        if val == a2[idx%8]:
            score[1] += 1
        if val == a3[idx%10]:
            score[2] += 1
            
    for idx, s in enumerate(score):
    	if s == max(score):
        	result.append(idx+1)
    return result
