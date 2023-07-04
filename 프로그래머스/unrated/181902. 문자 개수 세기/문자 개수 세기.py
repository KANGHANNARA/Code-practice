from string import ascii_lowercase
def solution(my_string):
    alphabet_list = list(ascii_lowercase)
    upper_list = [i.capitalize() for i in alphabet_list]
    answer = []
    for i in upper_list:
        answer.append(my_string.count(i))
    for i in alphabet_list:
        answer.append(my_string.count(i))
    
    return answer