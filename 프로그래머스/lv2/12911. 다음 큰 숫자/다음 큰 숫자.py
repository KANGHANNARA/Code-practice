def solution(n):
    answer = 0
    for a in range(n+1,1000001):
        if bin(n).count('1') == bin(a).count('1'):
            answer = a
            break
    return a