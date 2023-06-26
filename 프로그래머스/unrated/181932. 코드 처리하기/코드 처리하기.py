def solution(code):
    mode = True
    ret = ""
    for idx, i in enumerate(code):
        if mode:
            if i != "1" and idx % 2 == 0:
                ret = ret + i
            elif i == "1":
                mode = False
        else:
            if i != "1" and idx % 2 == 1 :
                ret = ret + i
            elif i == "1":
                mode = True
    if len(ret) == 0:
        return "EMPTY"
    return ret
                
