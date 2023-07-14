def solution(food):
    
    food_arrangement = []
    
    for i in range(1, len(food)):
        if(food[i] // 2 >= 1):
            for j in range(food[i] // 2):
                food_arrangement.append(i)
    
    sort_answer = sorted(food_arrangement, reverse = True)
    
    food_arrangement.append(0)
    
    answer = food_arrangement + sort_answer
    
    return ''.join(str(i) for i in answer)
   