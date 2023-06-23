def solution(str1, str2):
    res=''
    for s1,s2 in zip(str1,str2):
        res+=s1+s2
    return res
