def solution(arr, intervals):
    a = [arr[i[0]:i[1]+1] for i in intervals]
    answer = []
    for i in a:
         answer +=i
    return answer