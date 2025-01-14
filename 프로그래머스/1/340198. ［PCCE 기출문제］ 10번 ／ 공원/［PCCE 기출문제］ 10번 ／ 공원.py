def solution(mats, park):
    answer = 0  

    mats.sort()  

    for mat_size in mats:
        for i in range(len(park)):
            for j in range(len(park[i])):
                if i + mat_size <= len(park) and j + mat_size <= len(park[i]):
                    check = True
                    for x in range(i, i + mat_size):  
                        for y in range(j, j + mat_size):  
                            if park[x][y] != "-1":  
                                check = False
                                break
                    if check: 
                        answer = mat_size

    
    if answer > 0:
        return answer 
    else:
        return -1 