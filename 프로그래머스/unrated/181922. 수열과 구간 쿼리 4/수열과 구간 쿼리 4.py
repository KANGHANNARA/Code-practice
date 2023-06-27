def solution(arr, queries):
    answer = []
    for a, b, c in queries:
        for i, k in enumerate(arr[a:b+1]):
            if a+i % c == 0:
                arr[a+i] = k+1
    return arr