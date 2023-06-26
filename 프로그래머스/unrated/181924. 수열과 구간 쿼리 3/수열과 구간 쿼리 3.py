def solution(arr, queries):
    answer = []
    for i in queries:
        a = i[0]
        b = i[1]
        arr[a] ,arr [b]= arr[b] , arr[a]
    answer = arr
    return answer