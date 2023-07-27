import math
from itertools import *
def is_number(s):
    for i in range(2, int(math.sqrt(s) + 1)):
        if s % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if is_number(i) == True:
            answer += 1
    return answer