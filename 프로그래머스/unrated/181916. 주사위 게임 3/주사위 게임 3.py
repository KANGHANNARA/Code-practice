def solution(a, b, c, d):
    answer = 0
    qwer = [a,b,c,d]
    arr = list(set(qwer))
    
    if len(arr) == 4:
        answer = min(arr)
    elif len(arr) == 3:
        p = max(qwer, key=qwer.count)
        q = [num for num in arr if num!=p]
        answer = q[0] * q[1]
    elif len(arr) == 2:
        if max([qwer.count(num) for num in arr]) > 2:
            p = max(qwer, key=qwer.count)
            q = min(qwer, key=qwer.count)
            answer = pow((10 * p + q),2)
        else:
            x = arr[0]
            y = arr[1]
            answer = (x+y) * abs(x-y)
    elif len(arr) == 1:
        answer = int(str(arr[0]) * 4)
    return answer