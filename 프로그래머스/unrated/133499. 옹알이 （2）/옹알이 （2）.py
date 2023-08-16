def solution(babbling):
    answer = 0
    a = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for j in a:
            if (j in babbling[i]) and (j*2 not in babbling[i]):
                babbling[i] = babbling[i].replace(j,"*")
                
        if all(char == "*" for char in babbling[i]):
            answer +=1
    return answer