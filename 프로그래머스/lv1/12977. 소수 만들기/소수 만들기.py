import math
from itertools import *
def is_number(s):
    for i in range(2, int(math.sqrt(s) + 1)):
        if s % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    for i in combinations(nums,3):
        if is_number(sum(i))==True:
            answer += 1
        else:
            continue       
    return answer