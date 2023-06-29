from itertools import *

def solution(number):
    
    count = 0

    three_gun_student = list(combinations(number, 3))

    sums = [sum(tup) for tup in three_gun_student]

    for i in range(len(sums)):
        if(sums[i] == 0):
            count = count + 1
            
    return count