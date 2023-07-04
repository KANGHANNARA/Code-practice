def solution(arr):
    answer = []
    if 2 in arr:
        if arr.count(2) > 1: # 2가 2개 이상일 경우
            start = arr.index(2)
            end = len(arr) - arr[::-1].index(2) # 배열을 뒤집어서 2의 인덱스를 찾고 길이 만큼 빼면 끝의 2위치의 인덱스+1가 나옴
            return arr[start:end] # 처음과 끝의 2의 위치의 인덱스포함의 배열 리턴
        else:
            idx = arr.index(2) # 1일경우
            return [arr[idx]]
    else: # 없을경우
        return [-1]
    
    return answer