from itertools import *

def solution(numbers):
    
    sort_numbers = list(combinations(numbers, 2))
    
    
    arr_sort_numbers = [a*b for a, b in sort_numbers]
    
    
    return max(arr_sort_numbers)