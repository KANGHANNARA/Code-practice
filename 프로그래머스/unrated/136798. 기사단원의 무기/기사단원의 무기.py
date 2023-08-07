def solution(number, limit, power):
    answer = 0
    count = 0
    n_list = []
    for i in range(1,number+1):
        count = 0
        for j in range(1, int(i**(1/2)) + 1):
            if i%j == 0:
                count +=1
                if ( (j**2) != i):
                    count +=1
        n_list.append(count)
    for idx,val in enumerate(n_list):
        if val > limit:
            n_list[idx] = power
    return sum(n_list)