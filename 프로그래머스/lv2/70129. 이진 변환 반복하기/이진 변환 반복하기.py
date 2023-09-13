def solution(s):
    answer = []
    cnt = 0
    cnt2 = 0
    f = ""
    while len(f)!=1:
        f = s.replace('0','')
        cnt += 1
        cnt2 += len(s)-len(f)
        s = bin(len(f))[2:]
    
    answer.append(cnt)
    answer.append(cnt2)
    return answer