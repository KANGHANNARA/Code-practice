def solution(num):
    cnt = 0
    if num ==1:
        return 0
    while (cnt < 500 and num > 1):
        cnt+=1
        if num%2 == 0:
            num //= 2
        else:
            num = num*3+1

    return cnt if 500>cnt>0 else -1