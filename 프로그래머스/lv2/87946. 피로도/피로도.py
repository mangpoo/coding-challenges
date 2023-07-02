from itertools import *

def solution(k, dungeons):
    
    temp = -1

    sort_dungeons = list(permutations(dungeons, len(dungeons)))
    count = [0] * len(sort_dungeons)

    for i in sort_dungeons:
        temp += 1
        temp_k = k
        for j in range(len(i)):
            if(temp_k >= i[j][0]):
                temp_k -= i[j][1]
                count[temp] += 1
                
    return max(count)