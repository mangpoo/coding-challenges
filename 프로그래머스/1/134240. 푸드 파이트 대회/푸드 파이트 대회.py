def solution(food):
    del food[0]
    left_food_list = []
    right_food_list = []
    count = 0
    for i in food:
        count += 1
        eat_food = i // 2
        for j in range(0,eat_food):
            left_food_list.append(count)
            right_food_list.append(count)
    left_food_list.append(0)
    right_food_list.reverse()
    answer = ''.join(map(str, left_food_list + right_food_list))
    print(answer)
    return answer