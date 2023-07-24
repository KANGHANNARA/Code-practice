import datetime
def solution(a, b):
    date_dict = {0: 'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    date = '2021-10-21'
    answer = datetime.date(2016, a, b)
    
    return date_dict[answer.weekday()]