import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]
def solution(n):
    a = convert(n,3)
    answer = a[::-1]
    
    return int(answer,3)