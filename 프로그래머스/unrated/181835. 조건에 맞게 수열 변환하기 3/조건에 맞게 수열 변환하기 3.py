def solution(arr, k):
    a = []
    if k % 2 == 1 :
        for i in arr:
            a.append(i*k)
    else :
        for i in arr:
            a.append(i+k)
    return a