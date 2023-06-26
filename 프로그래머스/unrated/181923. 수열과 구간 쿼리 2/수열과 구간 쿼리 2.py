def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        a = []
        for val in arr[s:e+1]:
            if val > k:
                a.append(val)
        answer.append(-1 if not a else min(a))
    return answer