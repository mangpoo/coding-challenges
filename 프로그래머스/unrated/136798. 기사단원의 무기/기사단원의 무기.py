import math

def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                count += 2 if i // j != j else 1
        if count > limit:
            answer += power
        else:
            answer += count
        
    return answer