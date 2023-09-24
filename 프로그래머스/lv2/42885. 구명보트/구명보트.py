import itertools
def solution(people, limit):
    people.sort()
    answer = 0 # 2명의 사람을 구해서 나간 구명보트 
    a = 0 # 반복문의 첫번째 변수
    b = len(people)-1 # 반복문의 끝 변수 
    while a < b :
        if people[a] + people[b] <= limit :
            a += 1
            answer +=1
        b -= 1
    return len(people)-answer