def solution(n):
    
    num_list = list(map(int, str(n)))
    sum_num_list = 0
    
    for i in num_list:
        sum_num_list = sum_num_list + i
    
    print(sum_num_list)
    
    return sum_num_list