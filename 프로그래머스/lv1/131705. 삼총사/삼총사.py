def solution(number):
    Q = 0 
    l = len(number)
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                if number[i] + number[j] + number[k] == 0:
                    Q += 1
    return Q