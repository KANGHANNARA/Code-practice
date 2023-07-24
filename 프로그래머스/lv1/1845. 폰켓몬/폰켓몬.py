import numpy as np
import pandas as pd
def solution(nums):
    answer = 0
    a = len(nums)/2
    if a < len(list(set(nums))):
        answer = a
    else:
        answer = len(list(set(nums)))
    return answer