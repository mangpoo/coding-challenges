def solution(sides):
    
    c = max(sides)
    sides.remove(c)
    
    if(sides[0] + sides[1] > c):
        answer = 1
        return answer
    
    else:
        answer = 2
        return answer