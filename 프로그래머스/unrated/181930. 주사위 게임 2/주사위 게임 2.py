def solution(a, b, c):
    answer = 0
    x, y ,z = (a + b + c), (a**2 + b**2 + c**2 ), (a**3 + b**3 + c**3 )
    if a == b and b == c:
        answer = x * y * z
    elif a == b or b == c or c == a:
        answer = x * y
    else :
        answer = x
    return answer