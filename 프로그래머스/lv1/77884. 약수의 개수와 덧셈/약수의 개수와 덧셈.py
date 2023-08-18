def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        divisorsList = []
        for j in range(1, int(i**(1/2)) + 1):
            if (i % j == 0):
                divisorsList.append(j) 
                if ( (j**2) != i) : 
                    divisorsList.append(i // j)
        if (len(divisorsList))%2==0:
            answer += i
        else:
            answer -= i
    return answer