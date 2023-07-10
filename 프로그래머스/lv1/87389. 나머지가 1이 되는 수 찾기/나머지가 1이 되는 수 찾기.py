def solution(n):
    
    list = []
    
    for i in range(1 , n+1):
        if(n % i == 1):
            list.append(i)
    
    return min(list) if list else None